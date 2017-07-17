from django.test import TestCase

from django_nyt import notify, models

try:
    from django.contrib.auth import get_user_model
    User = get_user_model()
except ImportError:
    from django.contrib.auth.models import User


class NotifyTest(TestCase):
    
    def test_simple(self):
        
        TEST_KEY = 'test_key'
        TEST_USER = User.objects.create_user(
            'lalala'
        )
        
        TEST_NOTIFICATION_TYPE = models.NotificationType.objects.create(key=TEST_KEY)
        TEST_SETTINGS = models.Settings.objects.create(
            user=TEST_USER,
        )
        models.Subscription.objects.create(
            settings=TEST_SETTINGS,
            notification_type=TEST_NOTIFICATION_TYPE,
        )
        notify("Test Is a Test", TEST_KEY)
        
        self.assertEqual(models.Notification.objects.all().count(), 1)