import logging

import json
from lxml import html

from lems_ui.models import LemsElement, LemsModel

from lems.model import model, component
from lems.parser import LEMS

LOG = logging.getLogger(__name__)


def component_json_to_model_root_id(model_json):
        html_root = html.fromstring(json.loads(model_json)['instance_data'])
        components = {}
        for child in html_root.getchildren():
            if child.tag != 'div':
                continue
            comp_info = {
                    'lems_type': child.get('lems_type'),
                    'html': html.tostring(child),
                    'html_obj': child
            }
            c = comp_info['html_obj']

            try:
                id = c.xpath("div[@class='inst_id']/input")[0].get('value')
            except Exception as e:
                LOG.error(html.tostring(c))
            return id;

def component_json_to_lems_xml(model_json, component_top):
        html_root = html.fromstring(json.loads(model_json)['instance_data'])
        wantedId = component_top;
        # get a dict of component objects from the model_json
        components = {}
        for child in html_root.getchildren():
            if child.tag != 'div':
                continue
            components[child.get('id')] = {
                    'lems_type': child.get('lems_type'),
                    'html': html.tostring(child),
                    'html_obj': child
            }

        for comp_uid, comp_info in components.items():
            try:
                for key, val in parse_html_component(comp_info).items():
                    components[comp_uid][key] = val
            except Exception as e:
                return '<error>' + e.message + '</error>'


        # put components in their hierarchy and add to the model
        # add component types to lems_types_xml
        lems_types_xml = ''
        lems_model_obj = model.Model()
        for comp_uid in add_children(components):
            lems_model_obj.add_component(components[comp_uid]['lems_obj'])

            this_name = components[comp_uid]['lems_obj'].type

            while 1:
                lems_type = LemsElement.objects.get(lems_elem='component_types',
                                                    name=this_name)

                if lems_type.from_file.lower() == 'gui created':
                    lems_types_xml = lems_type.xml + '\n\n' + lems_types_xml
                    this_name = lems_type.extends
                else:
                    break


        # pull each component from the model and convert to xml
        lems_xml = ''
        for comp in lems_model_obj.components.values():
            if comp.id == wantedId:
                lems_xml += comp.toxml() + '\n\n'

            for comp2 in comp.children:
                if comp2.id == wantedId:
                    lems_xml += comp2.toxml() + '\n\n'


                for comp3 in comp2.children:
                    if comp3.id == wantedId:
                        lems_xml += comp3.toxml() + '\n\n'

                    for comp4 in comp3.children:
                        if comp4.id == wantedId:
                            lems_xml += comp4.toxml() + '\n\n'

        LOG.debug(lems_xml)

        full_xml = lems_types_xml + lems_xml

        # jlems doesn't like any '><'
        full_xml = full_xml.replace('><', '>  <')
        full_xml = full_xml.encode('utf-8')

        #grab out all the data to recreate the hierachy later
        components_ret = {}
        for component in (components):
            components_ret[components[component]['lems_obj'].id] = {'id' : component}
            components_ret[components[component]['lems_obj'].id]['id'] = component
            components_ret[components[component]['lems_obj'].id]['type'] = components[component]['lems_obj'].type
            components_ret[components[component]['lems_obj'].id]['parameters'] = components[component]['lems_obj'].parameters
            #print " components[component]['lems_obj'].type"
            #print  components[component]['lems_obj'].type
            components_ret[components[component]['lems_obj'].id]['child_dict'] =  components[component]['child_dict']
            components_ret[components[component]['lems_obj'].id]['children_dict'] =  components[component]['children_dict']
            components_ret[components[component]['lems_obj'].id]['comp_ref_dict'] =  components[component]['comp_ref_dict']

        for component in (components_ret):
            for child in (components_ret[component]['child_dict']):
                for component2 in (components_ret):
                    if components_ret[component]['child_dict'][child] == components_ret[component2]['id']:
                        components_ret[component]['child_dict'][child] = component2
                if not isinstance(components_ret[component]['child_dict'][child], basestring):
                    i = 0
                    for child2 in components_ret[component]['child_dict'][child]:
                        for component2 in (components_ret):
                            if components_ret[component]['child_dict'][child][i] == components_ret[component2]['id']:
                                components_ret[component]['child_dict'][child][i] = component2
                        i=i+1
            for child in (components_ret[component]['children_dict']):
                for component2 in (components_ret):
                    if components_ret[component]['children_dict'][child] == components_ret[component2]['id']:
                        components_ret[component]['children_dict'][child] = component2
                if not isinstance(components_ret[component]['children_dict'][child], basestring):
                    i = 0
                    for child2 in components_ret[component]['children_dict'][child]:
                        for component2 in (components_ret):
                            if components_ret[component]['children_dict'][child][i] == components_ret[component2]['id']:
                                components_ret[component]['children_dict'][child][i] = component2
                        i=i+1
            for child in (components_ret[component]['comp_ref_dict']):
                for component2 in (components_ret):
                    if components_ret[component]['comp_ref_dict'][child] == components_ret[component2]['id']:
                        components_ret[component]['comp_ref_dict'][child] = component2
                if not isinstance(components_ret[component]['comp_ref_dict'][child], basestring):
                    i = 0
                    for child2 in components_ret[component]['comp_ref_dict'][child]:
                        for component2 in (components_ret):
                            if components_ret[component]['comp_ref_dict'][child][i] == components_ret[component2]['id']:
                                components_ret[component]['comp_ref_dict'][child][i] = component2
                        i=i+1

        components_ret2 = {}
        components_ret2 = addComponent(components_ret,{},wantedId)

        return {'xml':full_xml,'components' : components_ret2 }


def addComponent(components_ret,hierarchy,component):
    hierarchy[component] = {}
    hierarchy[component]['comp_ref_dict'] = components_ret[component]['comp_ref_dict']
    hierarchy[component]['children_dict'] = components_ret[component]['children_dict']
    hierarchy[component]['child_dict'] = components_ret[component]['child_dict']
    hierarchy[component]['id'] = component
    hierarchy[component]['type'] = components_ret[component]['type']
    hierarchy[component]['parameters'] = components_ret[component]['parameters']

    for child in (hierarchy[component]['child_dict']):
        if not isinstance(hierarchy[component]['child_dict'][child], basestring):
            i = 0
            for child2 in hierarchy[component]['child_dict'][child]:
                for component2 in (components_ret):
                    #print("hierarchy[component]['child_dict'][child]")
                    #print hierarchy[component]['child_dict'][child]
                    if hierarchy[component]['child_dict'][child][i] == component2:
                        hierarchy[component]['child_dict'][child][i] = {}
                        addComponent(components_ret,hierarchy[component]['child_dict'][child][i],component2)
                i=i+1
        for component2 in (components_ret):
            if hierarchy[component]['child_dict'][child] == component2:
                #hierarchy[component]['child_dict'][child] = components_ret[component2]
                hierarchy[component]['child_dict'][child] = {}
                addComponent(components_ret,hierarchy[component]['child_dict'][child],component2)
    for child in (hierarchy[component]['children_dict']):
        if not isinstance(hierarchy[component]['children_dict'][child], basestring):
            i = 0
            for child2 in hierarchy[component]['children_dict'][child]:
                for component2 in (components_ret):
                    if hierarchy[component]['children_dict'][child][i] == component2:
                        hierarchy[component]['children_dict'][child][i] = {}
                        addComponent(components_ret,hierarchy[component]['children_dict'][child][i],component2)
                i=i+1
        for component2 in (components_ret):
            if hierarchy[component]['children_dict'][child] == component2:
                hierarchy[component]['children_dict'][child] = {}
                addComponent(components_ret,hierarchy[component]['children_dict'][child],component2)
    for child in (hierarchy[component]['comp_ref_dict']):
        if not isinstance(components_ret[component]['comp_ref_dict'][child], basestring):
            i = 0
            for child2 in hierarchy[component]['comp_ref_dict'][child]:
                for component2 in (components_ret):
                    #print("hierarchy[component]['comp_ref_dict'][child]")
                    #print hierarchy[component]['comp_ref_dict'][child]
                    if hierarchy[component]['comp_ref_dict'][child][i] == component2:
                        hierarchy[component]['comp_ref_dict'][child][i] = {}
                        addComponent(components_ret,hierarchy[component]['comp_ref_dict'][child][i],component2)
                i=i+1
        for component2 in (components_ret):
            if hierarchy[component]['comp_ref_dict'][child] == component2:
                hierarchy[component]['comp_ref_dict'][child] = {}
                addComponent(components_ret,hierarchy[component]['comp_ref_dict'][child],component2)
    return hierarchy;


def model_json_to_lems_xml(model_json, include_hier=False, syn_ids=None, include_header=True, include_Components=True):
        html_root = html.fromstring(json.loads(model_json)['instance_data'])

        # get a dict of component objects from the model_json
        components = {}
        for child in html_root.getchildren():
            if child.tag != 'div':
                continue
            components[child.get('id')] = {
                    'lems_type': child.get('lems_type'),
                    'html': html.tostring(child),
                    'html_obj': child
            }

        for comp_uid, comp_info in components.items():
            try:
                for key, val in parse_html_component(comp_info).items():
                    components[comp_uid][key] = val
            except Exception as e:
                return '<error>' + e.message + '</error>'


        # put components in their hierarchy and add to the model
        # add component types to lems_types_xml
        lems_types_xml = ''
        lems_model_obj = model.Model()
        for comp_uid in add_children(components):
            lems_model_obj.add_component(components[comp_uid]['lems_obj'])

            this_name = components[comp_uid]['lems_obj'].type

            while 1:
                lems_type = LemsElement.objects.get(lems_elem='component_types',
                                                    name=this_name)

                if lems_type.from_file.lower() == 'gui created':
                    lems_types_xml = lems_type.xml + '\n\n' + lems_types_xml
                    this_name = lems_type.extends
                else:
                    break


        # pull each component from the model and convert to xml
        lems_xml = ''
        for comp in lems_model_obj.components.values():
            lems_xml += comp.toxml() + '\n\n'

        LOG.debug(lems_xml)

        syn_xml = ''
        if syn_ids:
            # Recursive
            for syn_id in syn_ids:
                syn_xml += model_json_to_lems_xml(LemsModel.objects.get(id=syn_id).json,
                                                  include_hier=True,
                                                  include_header=False)

        # build the final output, header, component types, components and closing tag
        LEMS_HEADER = '<?xml version="1.0" ?>\n<Lems xmlns="http://www.neuroml.org/lems/0.7.3" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.neuroml.org/lems/0.7.3 https://raw.github.com/LEMS/LEMS/development/Schemas/LEMS/LEMS_v0.7.3.xsd">'

        if( include_header ):
            if include_Components:
                full_xml = (LEMS_HEADER + '\n\n' + lems_types_xml + lems_xml + syn_xml + '</Lems>\n')
            else:
                full_xml = (LEMS_HEADER + '\n\n' + lems_xml + syn_xml + '</Lems>\n')
                    #lems_xml[lems_xml.find('<Component') :] )
        else:
            if include_Components:
                full_xml = lems_types_xml + lems_xml + syn_xml
            else:
                full_xml = lems_xml + syn_xml

        # jlems doesn't like any '><'
        full_xml = full_xml.replace('><', '>  <')
        full_xml = full_xml.encode('utf-8')
        return full_xml


def add_children(components_info):
    top_level_comps = components_info.keys()

    for comp_info in components_info.values():
        for child_name, child_uid in comp_info['child_dict'].items():
            components_info[child_uid]['lems_obj'].set_parameter('name', child_name)
            comp_info['lems_obj'].add(components_info[child_uid]['lems_obj'])
            if child_uid in top_level_comps: #FK fix for issue with boyle cohen model
                top_level_comps.remove(child_uid)

        for child_name, child_uid_list in comp_info['children_dict'].items():
            for child_uid in child_uid_list:
                components_info[child_uid]['lems_obj'].set_parameter('name', child_name)
                comp_info['lems_obj'].add(
                                    components_info[child_uid]['lems_obj'])
                if child_uid in top_level_comps: #FK fix for issue with boyle cohen model
                    top_level_comps.remove(child_uid)

        for name, uid in comp_info['comp_ref_dict'].items():
            comp_info['lems_obj'].set_parameter(name,
                                    components_info[uid]['lems_obj'].id)

    return top_level_comps


def parse_html_component(comp_info):
    c = comp_info['html_obj']

    try:
        id = c.xpath("div[@class='inst_id']/input")[0].get('value')
    except Exception as e:
        LOG.error(html.tostring(c))
        return {}

    LOG.debug('Parsing component: ' + id + ' : ' + comp_info['lems_type'])
    comp = model.Component(id,
                           comp_info['lems_type'])

    parse_errors = []

    # Add params as key, value
    for param in c.xpath("div[@class='params']/input"):

        # Get unit if present
        unit = ''
        it = param.itersiblings()
        sel = it.next()
        if sel.tag == 'select':
            unit = sel.xpath('option[@selected]')[0].text


        if(not param.get('value')):
            parse_errors.append('Empty Parameter [' + str(param.get('id')) +
                                '], Component [' + id + ']')

        comp.set_parameter(param.get('id'), param.get('value') + unit)

    # Get child dict
    child_dict = {}
    for child_item in c.xpath("div[@class='child_list']/button"):
        it = child_item.itersiblings()
        link = it.next()
        if link.tag == 'a':
            child_dict[child_item.get('id')] = link.get('id')[5:]

    # Get children dict
    children_dict = {}
    for children_item in c.xpath("div[@class='children_list']/button"):
        it = children_item.itersiblings()

        try:
            while(1):
                link = it.next()
                if link.tag == 'a':
                    if not children_dict.has_key(children_item.get('id')):
                        children_dict[children_item.get('id')] = []
                    children_dict[children_item.get('id')].append(
                                                    link.get('id')[5:])
        except:
            # END OF CHILDREN
            pass

    # Get comp ref dict
    comp_ref_dict = {}
    for comp_ref_item in c.xpath("div[@class='comp_refs']/button"):
        it = comp_ref_item.itersiblings()
        link = it.next()
        if link.tag == 'a':
            comp_ref_dict[comp_ref_item.get('id')] = link.get('id')[5:]

    if parse_errors:
        raise Exception(str(parse_errors))

    return {'lems_obj': comp,
            'child_dict': child_dict,
            'children_dict': children_dict,
            'comp_ref_dict': comp_ref_dict}


