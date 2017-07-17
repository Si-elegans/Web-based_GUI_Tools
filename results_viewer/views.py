from django.shortcuts import render

# Create your views here.
import logging
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from cenet.models import Neuron, SynapticConn, CENetwork
from lems_ui.models import Lems2FpgaJob
from lems_ui.jobExecution import runCheck

LOG = logging.getLogger(__name__)


@login_required
def results_viewer(rq):
    sim_id = rq.GET['sim_id']


    return render(rq, 'results_viewer/results_viewer.html',
                  {'user':rq.user, 'sim_id':sim_id, 'neurons' : Neuron.objects.order_by('name')})


@login_required
def results_viewer_ind(rq):
    sim_id = rq.GET['sim_id']

    runCheck()

    job = Lems2FpgaJob.objects.get(id=int(sim_id[15:]))
    if job.status == 3:
        return HttpResponse("Error in model execution: " + job.lems2fpga_message);

    return render(rq, 'results_viewer/results_viewer_ind.html',
                  {'user':rq.user, 'sim_id':sim_id, 'neurons' : Neuron.objects.order_by('name')})
