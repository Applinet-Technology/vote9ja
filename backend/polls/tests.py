

import datetime

from django.test import TestCase
from django.utils import timezone
# Create your tests here.

from .models import FGPoll

class FGPollModelTests(TestCase):
    def test_was_activated_recently_with_old_polls(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is older than 1 day.
        """
        time = timezone.now() - datetime.timedelta(days=1, seconds=1)
        old_poll = FGPoll(activation_date=time)
        self.assertIs(old_poll.was_activated_recently(), False)
    
    def test_was_activated_recently_with_recent_poll(self):
        """
        was_activated_recently() returns True for polls whose activation_date
        is within the last day.
        """
        time = timezone.now() - datetime.timedelta(hours=23, minutes=59, seconds=59)
        recent_poll = FGPoll(activation_date=time)
        self.assertIs(recent_poll.was_activated_recently(), True)