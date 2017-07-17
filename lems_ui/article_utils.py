import urllib
import logging

from django.db.models import Q

from lems_ui.models import LemsModel, Lems2FpgaJob, MODEL_TYPES, is_curator
from utils import model_json_to_lems_xml

try:
    from wiki.models import URLPath, ArticleRevision
    from jobExecution import runCheck
    __CREATE_ARTICLES = True
    print("__CREATE_ARTICLES = True")
except:
    __CREATE_ARTICLES = False
    print("__CREATE_ARTICLES = False")

LOG = logging.getLogger(__name__)

def create_article(rq, model,synId):
    response = ""

    if not __CREATE_ARTICLES:
        LOG.debug('No articles created : __CREATE_ARTICLES = False')
        response = 'No articles created : __CREATE_ARTICLES = False'
    elif( is_curator(rq.user) and model.public and
        model.model_type == MODEL_TYPES.NEURON ):

        lemsComp = model_json_to_lems_xml(model.json,include_hier=False,
                                          syn_ids=None,
                                          include_header=False,
                                          include_Components=False)

        lems_model = LemsModel.objects.get(id=int(model.pk))


        lems_model_synapse = LemsModel.objects.get(pk=synId)

        # Check for parse errors
        lems_xml = model_json_to_lems_xml(lems_model.json)
        lems_xml_synapse = model_json_to_lems_xml(lems_model_synapse.json)
        if lems_xml.startswith('<error>'):
            return 'Unable to create Model XML:\n' + lems_xml
        if lems_xml_synapse.startswith('<error>'):
            return 'Unable to create Synapse XML:\n' + lems_xml_synapse

        # Create entry in the jobs table, get id of new entry
        job = Lems2FpgaJob()
        job.owner = rq.user
        job.lems_model = lems_model
        job.syn_ids = synId
        # sim_type = 0 => jlems sim
        job.sim_type = 0
        job.status = 0
        job.save()

        try:
            runCheck()
        except:
            response = "Failure to run test job"

        pathTop = "neural_response_model_history_user/"
        slug = urllib.quote_plus(model.name)
        path = pathTop + slug;
        content = "Description \r\n" \
              "------------------\r\n" \
              "" + model.description + "\r\n" \
              "\r\n" \
              "Components \r\n" \
              "------------------\r\n" \
              "    " + lemsComp.replace("\n","\n    ") + "\r\n" \
              "Simulation Results \r\n" \
              "------------------\r\n" \
              "[Simulation Results link](https://platform.si-elegans.eu/djlems/results_viewer_ind/?sim_id=neuronModelTest" + str(job.pk) + ") \r\n\r\n" \
              "Use Model \r\n" \
              "------------------\r\n" \
              "[Copy Model from here](https://platform.si-elegans.eu/djlems/neuron_model/" + str(model.name) + "/) \r\n\r\n" \
              "More Info~ \r\n" \
              "------------------\r\n"
        summary = "Automated model update by curator"

        #save model to the wiki
        try:
            urlpath = URLPath.get_by_path(path, select_related=True)
            article = urlpath.article
            revision = ArticleRevision()
            revision.inherit_predecessor(article)
            revision.title = model.name
            index = article.current_revision.content.find("More Info~ \r\n" \
                  "------------------\r\n")
            oldMoreInfo = ""
            if index > -1:
                oldMoreInfo = article.current_revision.content[index + 32:]
            revision.content = content + oldMoreInfo
            revision.user_message = summary
            revision.deleted = False
            revision.set_from_request(rq)
            article.add_revision(revision)
            response = 'article created'
        except:
            urlpathParent = URLPath.get_by_path(pathTop, select_related=True)
            article = URLPath.create_article(
                    urlpathParent,
                    slug,
                    title=model.name,
                    content=content,
                    user_message=summary,
                    user=rq.user,
                    ip_address=None,
                    article_kwargs={'owner': rq.user,
                                    'group': None,
                                    'group_read': True,
                                    'group_write': True,
                                    'other_read': True,
                                    'other_write': True,
                                    })

        article.save()
        response = 'article updated'

    return response

