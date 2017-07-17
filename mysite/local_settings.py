# -*- coding: utf-8 -*-  
from spirit.settings import *

"""
Django settings for mysite project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys


BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ' '

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/dashboard' #GE: This tells the program where to go if login succesful and has no Next page value
ALLOWED_HOSTS = []
# Setting for django registration
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = '@gmail.com'
EMAIL_HOST_PASSWORD = ''
SERVER_EMAIL = '@gmail.com'
DEFAULT_FROM_EMAIL = ''
ACCOUNT_ACTIVATION_DAYS = 7

#
ACCOUNT_HANDLING = False

SITE_ID = 1

# Application definition

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Uncomment the next line to enable the admin:
    'django.contrib.admin',
    'siteLogic',
    'django.contrib.humanize',
    'django_nyt',
    'mptt',
    'sekizai',
    'sorl.thumbnail',
    'wiki',
    'wiki.plugins.attachments',
    'wiki.plugins.notifications',
    'wiki.plugins.images',
    'wiki.plugins.macros',    
    'django_notify',
    'spirit',
    'djconfig',
    'haystack',
    'social.apps.django_app.default',
    'registration',
    'storages',
    'debug_toolbar',
    'behaviouralExperimentDefinition',
    'rest_framework',
    'django_extensions',
    'booking',
    "sslserver",
    "lems_ui",
    "cenet",
    "results_viewer",
    "rtw_ui",
    "worm_conf",
    #'file_sharing',
    # Uncomment the next line to enable admin documentation:
    # 'django.contrib.admindocs',
)
REST_FRAMEWORK = {    
    'DEFAULT_PERMISSION_CLASSES': [
        
        'rest_framework.permissions.IsAdminUser',
        #'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly',  #Allows readOnly (GET) to all users, and applies DjangoModelPermissions to others
        #'rest_framework.permissions.AllowAny', #No permission, open for all
    ],
    #By default Session authentication is enabled, but I think that the following example enables both session and basic
    #Session authentication is good when the call to the rest interface is inside a http session, using the authentication done beforehand
    #Basic or token authentication is more targeted towards non-http application such as the mobile applications
    'DEFAULT_AUTHENTICATION_CLASSES': [        
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ],
    'DEFAULT_PARSER_CLASSES': (
        'rest_framework.parsers.JSONParser',
        'rest_framework_xml.parsers.XMLParser',
    ),
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
        'rest_framework_xml.renderers.XMLRenderer',
    ),
}        
AUTHENTICATION_BACKENDS = (
      'social.backends.open_id.OpenIdAuth',
      'social.backends.google.GoogleOpenId',
      'social.backends.google.GoogleOAuth2',
      'social.backends.google.GoogleOAuth',
      'social.backends.google.GooglePlusAuth',
      'social.backends.twitter.TwitterOAuth',
      'social.backends.yahoo.YahooOpenId',    
      'django.contrib.auth.backends.ModelBackend',
  )

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    "sekizai.context_processors.sekizai",
    'social.apps.django_app.context_processors.backends',
    'social.apps.django_app.context_processors.login_redirect',
    "siteLogic.views.google_login",
)

SOUTH_MIGRATION_MODULES = {
    'django_nyt': 'django_nyt.south_migrations',
    'wiki': 'wiki.south_migrations',
    'images': 'wiki.plugins.images.south_migrations',
    'notifications': 'wiki.plugins.notifications.south_migrations',
    'attachments': 'wiki.plugins.attachments.south_migrations',
}
MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    #'django.views.decorators.csrf._EnsureCsrfCookie',
    #http://www.rkblog.rk.edu.pl/w/p/making-django-and-javascript-work-nicely-together/ =>
    #Using beforeSend we can set the X-CSRFToken token. It's almost done.
    #If your browser has the "csrftoken" cookie the request will work, but if it's not there it will still fail.
    #Django won't make the cookie if it's not needed. To ensure cookie existence add
    #'django.views.decorators.csrf._EnsureCsrfCookie', to MIDDLEWARE_CLASSES.
)

SOCIAL_AUTH_GOOGLE_PLUS_KEY = ''
SOCIAL_AUTH_GOOGLE_PLUS_SECRET = ''
SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = ''
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = ''
SOCIAL_AUTH_STRATEGY = 'social.strategies.django_strategy.DjangoStrategy'
SOCIAL_AUTH_STORAGE = 'social.apps.django_app.default.models.DjangoStorage'
# It does not apply the command below if it is not preceded by:
SOCIAL_AUTH_GOOGLE_OAUTH2_SCOPE = [
   'https://www.googleapis.com/auth/plus.login','email']
SOCIAL_AUTH_GOOGLE_PLUS_IGNORE_DEFAULT_SCOPE = True
SOCIAL_AUTH_GOOGLE_PLUS_SCOPE = [
   'https://www.googleapis.com/auth/plus.login','email']
#    'https://www.googleapis.com/auth/userinfo.profile'

SOCIAL_AUTH_PIPELINE = (
    'social.pipeline.social_auth.social_details',
    'social.pipeline.social_auth.social_uid',
    'social.pipeline.social_auth.auth_allowed',
    'social.pipeline.social_auth.social_user',
    'social.pipeline.social_auth.associate_by_email',
    'social.pipeline.user.get_username',
    'social.pipeline.user.create_user',
    'social.pipeline.social_auth.associate_user',
    'social.pipeline.social_auth.load_extra_data',   
    'social.pipeline.user.user_details',
    # 'siteLogic.pipeline.saveAvatar'
)

SOCIAL_AUTH_DISCONNECT_PIPELINE = (
    #http://stackoverflow.com/questions/20589948/python-social-auth-notallowedtodisconnect-at-disconnect-facebook-1
    #'social.pipeline.disconnect.allowed_to_disconnect',
    'social.pipeline.disconnect.get_entries',
    'social.pipeline.disconnect.revoke_tokens',
    'social.pipeline.disconnect.disconnect',
    'siteLogic.views.logoutPipeline'
)

#If you want to revoke a provider's tokens on disconnect, define this setting:

SOCIAL_AUTH_REVOKE_TOKENS_ON_DISCONNECT = False

#Currently only handled for Facebook and Google-OAuth2. Some providers (e.g. Twitter) do not support revoking tokens from your app at all.
#From old django-social-auth module, we're using python-social-auth which is based on the previous one

#omab commented on 16 Feb
#https://github.com/omab/python-social-auth/issues/316#issuecomment-74483529
#@epetxepe, disconnect will remove the association between the google account and the user in your db, you will need association by email to reconnect that account later.

#Authentication Pipeline =>
#Email association (associate_by_email pipeline entry) is disabled by default for security reasons. Take for instance this scenario:
#
#User A registers using django-social-auth and we get email address foo@bar.com.
#User B goes to provider XXX and registers using foo@bar.com (provider XXX doesn’t validate emails).
#User B goes to your site and logs in using its XXX account using django-social-auth.
#User B gets access to User A account.



SOCIAL_AUTH_USER_MODEL = 'spirit.User'

AUTH_USER_MODEL = 'spirit.User'
    
ROOT_URLCONF = 'mysite.urls'

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR,'db.djangodb'),#Changed to get this workin in case of local deployment with apache mod_wsgi
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}
    ###################################
    # s3 storage
    ###################################

STATIC_URL ='/static/'

MEDIA_URL = '/media/'
STATIC_ROOT =  os.path.join(BASE_DIR,"static")
MEDIA_ROOT =  os.path.join(BASE_DIR,"media")
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,"static-src"),
)
# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Template location
TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,"templates"),    
)
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

INTERNAL_IPS = ('')
SUPPORT_MAILING_LIST = ''
    
U_LOGFOLDER = ''
U_LOGFILE_NAME = 'django_log.txt'
U_LOGFILE_SIZE = 1 * 1024 * 1024
U_LOGFILE_COUNT = 2
U_LOGFILE_BOOKING = 'booking'
U_LOGFILE_APP2 = 'app2'
ADMINS = (
  ('', SUPPORT_MAILING_LIST),
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {        
        'verbose': {
            'format': u'%(levelname)s %(asctime)s %(pathname)s %(module)s %(funcName)s %(lineno)d %(message)s'
        },
        'simple': {
            'format': u'%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            #'filters': ['require_debug_false'],
            #Default AdminEmailHandler is sync, use threaded option https://code.djangoproject.com/ticket/19214
            'class': 'siteLogic.utils.AdminEmailHandlerThreaded',
            'formatter': 'verbose',
        },
        'logfile': {
            'level':'DEBUG',
            'class':'logging.handlers.RotatingFileHandler',
            'filename': U_LOGFOLDER+U_LOGFILE_NAME,
            'maxBytes': U_LOGFILE_SIZE,
            'backupCount': U_LOGFILE_COUNT,
            'formatter': 'verbose',
        },
        'stderr': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'stream': sys.stderr,
            'formatter': 'verbose',
        },
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        #One logger per APP even if they use the same file, needs to be specified per file
        'siteLogic': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'booking': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'behaviouralExperimentDefinition': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'restAPI': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
        'restAPI': {
            'handlers': ['logfile'],
            'level': 'DEBUG',
            'propagate': True,
        },
        #U_LOGFILE_BOOKING, which passes all messages at DEBUG or higher that also pass the
        #special filter to two handlers – the logfile, and mail_admins.
        #This means that all DEBUG level messages (or higher) will be written to the logfile;
        #ERROR and CRITICAL messages will also be output via email.
        
        U_LOGFILE_BOOKING: {
            'handlers': ['logfile','mail_admins'],            
            'level': 'DEBUG',
            'propagate': True,
        },        
    }
}   
