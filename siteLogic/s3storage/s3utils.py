#!/usr/bin/env python
from storages.backends.s3boto import S3BotoStorage

class MediaS3BotoStorage(S3BotoStorage):
    location = 'media'
class StaticS3BotoStorage(S3BotoStorage):
    location = 'static'

#Fix based on the post at http://stackoverflow.com/questions/14266950/wrong-url-with-django-sorl-thumbnail-with-amazon-s3