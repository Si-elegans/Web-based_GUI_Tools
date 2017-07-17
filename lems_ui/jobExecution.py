"""
Simple XML-RPC Client to send simulations to lems2fpga
"""
import os
#os.environ['DJANGO_SETTINGS_MODULE'] = 'djlems.settings'

from django.core.files import File
import json
import time
import xmlrpclib
#import djlems.settings
from utils import model_json_to_lems_xml,component_json_to_model_root_id
from lems_ui.models import LemsModel, Lems2FpgaJob

SIM_TIME = 0.5
SIM_TIME_STEP = 0.00005

jobPrepend = "neuronModelTest"
server_address = 'http://152.71.254.9:444/lems2vhdl/xmlrpc'

def convert(server, job):
    # Update status to 'Running'
    job.status = 1
    job.save()

    syn_ids = None
    print ('syn ids')
    print(job.syn_ids)
    if job.syn_ids:
        syn_ids = job.syn_ids.split('_')[:-1]
    print(syn_ids)
    syn_ids = [job.syn_ids]
    lems_text = model_json_to_lems_xml(job.lems_model.json, syn_ids=syn_ids)
    lems_neuron_model_id = component_json_to_model_root_id(job.lems_model.json)
    if lems_text.startswith('<error>'):
        job.status = 3
        msg = "Lems parse error: " + lems_text
        job.lems2fpga_message = msg
        print msg
        job.save()
        return

    print ("server.Lems2VHDL.convertSingleModel\n\t" +
            job.owner.username + ",\n\t" +
            jobPrepend + str(job.id) + ",\n\t" +
            lems_text + ",\n\t" +
            lems_neuron_model_id + ",\n\t" +
            str(job.sim_type==0) + ", " + str(job.sim_type==1) + ", " +
            str(job.sim_type==2) + ", " + "False, False,\n\t" +
            str(SIM_TIME) + ", " + str(SIM_TIME_STEP))

    try:
        results = server.Lems2VHDL.convertSingleModel(
                    job.owner.username,
                    jobPrepend + str(job.id),
                    "\n".join(lems_text.splitlines()[2:-1]),
                    lems_neuron_model_id,
                    job.sim_type==0, job.sim_type==1, job.sim_type==2,
                    False, False, SIM_TIME, SIM_TIME_STEP)

        print "Received results: " + str(results)
        results = json.loads(results)

    except Exception as e:
        job.status = 3
        msg = "Exception from conversion server: " + str(e)
        job.lems2fpga_message = msg
        print msg
        job.save()
        return

    if results['code'] == 501 or results['code'] == 502:
        job.status = 0
        BACKOFF = True

    job.lems2fpga_code = results['code']
    job.lems2fpga_message = results['message']
    job.lems2fpga_job_id = results['jobId']
    job.save()
    print "Server response: " + results['message'] + " ; Job: " + str(job)
    return

def check_status(server, job):

    try:
        results = server.Lems2VHDL.getJobStatus(
                    job.lems2fpga_job_id)

        print "job status " + str(results)
        results = json.loads(results)

    except Exception as e:
        job.status = 3
        job.lems2fpga_message = "Exception from conversion server: " + str(results)
        job.save()
        return

    if results['code'] == 200:
        job.status=2
    if results['code'] >=400 and results['code'] <=500:
        job.status=3

    job.lems2fpga_code = results['code']
    job.lems2fpga_message = results['message']
    job.save()
    return


def runCheck():
    server = xmlrpclib.Server(server_address)

    # run a test command - it'll throw an exception if server's not running
    print '1 + 2 = ' + str(server.Calculator.add(1, 2))

    # keep going until ctrl-c'd, TODO: clean exit

    jobs = []

    jobs = Lems2FpgaJob.objects.filter(status=1). \
                                       order_by('updated')

    if len(jobs) > 0:
        print "Checking status of job: " + str(jobs[0])
        check_status(server, jobs[0])
        #time.sleep(5)


    # Get latest waiting job
    jobs = Lems2FpgaJob.objects.filter(status = 0). \
                                       order_by('updated')
    if len(jobs) > 0:
        print "Running Job: " + str(jobs[0])
        convert(server, jobs[0])


    # Wait before going round again
    #time.sleep(2)
