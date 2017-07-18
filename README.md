# Si elegans Web-based GUI Tools
Web-based Interfaces for Virtual C. elegans Neuron Model Definition, Network Configuration, Behavioural Experiment Definition and Experiment Results Visualisation

This repository contains the open source code of the web-based GUI tools developed within the [[FP7 Si-elegans project](https://www.si-elegans.eu)]. Our goal is to open the developed web-tools to the community.

The web-based GUI tools running instance is available at: [[Si-elegans platform online](https://platform.si-elegans.eu)]

## Local setup instructions (Tested with python 2.7 in both Windows 10 and Ubuntu 14.04)

0.- Clone repository

1.- Create & activate virtualenv 

2.- pip install -r requirements_local.txt

3.- python manage.py migrate --settings=mysite.local_settings

4.- python manage.py loaddata sielegans-fixture.json --settings=mysite.local_settings

5.- python manage.py loaddata cenet-fixture.json --settings=mysite.local_settings

6.- python manage.py loaddata lems_ui-fixture.json --settings=mysite.local_settings

7.- python manage.py createcachetable spirit_cache --settings=mysite.local_settings

8.- python manage.py runsslserver --addrport 0.0.0.0:8000 --settings=mysite.local_settings

9.- Open https://127.0.0.1:8000 in your browser. (**https!!**)

## Notes:
* Source code includes examples for Neuron models, Network configuration, Behavioural experiments and results. (See fixtures loaded in local setup instructions).
* Some external modules had to be fixed / modified during integration within the Web-GUI tools, therefore they are included as folders in the source code.  (i.e. django_notify, django_nyt, registration, spirit and wiki)
* This development uses [[Spirit forum](http://spirit-project.com/)] user extension of the strandard Django user. 
* Emulation logic is not included. The Si elegans project includes a  FPGA-based emulation, but web-based GUI tools could be integrated with software-based simulation frameworks.  
* Emulation dependent GUI's functionality might have limitations in the provided repository setup.
* Configuration keys for certain services have been deleted from code, so some services will not directly work (e.g. mailing (for account registration, for error reporting, ...), Google account-based login, Amazon Web Services)
* Amazon Web Services deployment configuration files are included (i.e. requirements.txt and mysite.settings.py) - This configuration requires filling some account info - Will not directly work as provided.


Contact: sielegans.webplatform@gmail.com


   
