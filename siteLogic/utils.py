#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
This function is defined to avoid errors UnicodeDecodeError: 'ascii' codec can't decode byte 0xf3 in position 205: ordinal not in range(128)
Explanation:
http://agiliq.com/blog/2014/12/understanding-python-unicode-str-unicodeencodeerro/
Fix from:
https://github.com/boundlessgeo/suite-qgis-plugin/commit/8ce6a09126f44337ab85f2f3a29604cb817997c1
'''
def secure_exception_to_str (e):
    string = unicode(str(e.message), errors = "ignore").encode('utf-8')
    return string

import threading

# Class for running a function in another thread. TODO: Use this for the code in gcm and email2.
class FuncThread(threading.Thread):
    def __init__(self, target, *args, **kwargs):
        self._target = target
        self._args = args
        self._kwargs = kwargs
        threading.Thread.__init__(self)

    def run(self):
        self._target(*self._args, **self._kwargs)

import logging
import traceback

from django.conf import settings
from django.core import mail
from django.views.debug import ExceptionReporter, get_exception_reporter_filter


class AdminEmailHandlerThreaded(logging.Handler):
    """An exception log handler that ASYNCHRONOUSLY emails log entries to site admins.

    If the request is passed as the first argument to the log record,
    request data will be provided in the email report.

    The default one is blocking, which is a little silly.
    """

    def __init__(self, include_html=False):
        logging.Handler.__init__(self)
        self.include_html = include_html

    def emit(self, record):
        try:
            request = record.request
            subject = '%s (%s IP): %s' % (
                record.levelname,
                (request.META.get('REMOTE_ADDR') in settings.INTERNAL_IPS
                 and 'internal' or 'EXTERNAL'),
                record.getMessage()
            )
            filter = get_exception_reporter_filter(request)
            request_repr = filter.get_request_repr(request)
        except Exception:
            subject = '%s: %s' % (
                record.levelname,
                record.getMessage()
            )
            request = None
            request_repr = "Request repr() unavailable."
        subject = self.format_subject(subject)

        if record.exc_info:
            exc_info = record.exc_info
            stack_trace = '\n'.join(traceback.format_exception(*record.exc_info))
        else:
            exc_info = (None, record.getMessage(), None)
            stack_trace = 'No stack trace available'

        message = "%s\n\n%s" % (stack_trace, request_repr)
        reporter = ExceptionReporter(request, is_email=True, *exc_info)
        html_message = self.include_html and reporter.get_traceback_html() or None
        FuncThread(mail.mail_admins, subject, message, fail_silently=True, html_message=html_message).start()

    def format_subject(self, subject):
        """
        Escape CR and LF characters, and limit length.
        RFC 2822's hard limit is 998 characters per line. So, minus "Subject: "
        the actual subject must be no longer than 989 characters.
        """
        formatted_subject = subject.replace('\n', '\\n').replace('\r', '\\r')
        return formatted_subject[:989]