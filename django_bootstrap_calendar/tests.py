# -*- coding: utf-8 -*-
__author__ = 'juliocesar'

from datetime import timedelta
from django.test import TestCase
from django.utils import datetime_safe, timezone
from django_bootstrap_calendar.models import CalendarEvent
from django_bootstrap_calendar.serializers import event_serializer


class EventSerializerTest(TestCase):

    def test_serializer_json_with_an_event(self):
        """
        Create a ``CalendarEvent`` and test if serialize function returns the
        correct json.

        The :class:`~django_bootstrap_calendar.models.CalendarEvent` is
        created with 5 hours duration.
        """
        timestamp = datetime_safe.datetime(2014, 03, 16, 12, 30,
                                           tzinfo=timezone.UTC())
        event = CalendarEvent.objects.create(
            title="Some Event Test",
            start=timestamp,
            end=timestamp + timedelta(seconds=60*60*5),
            url='http://example.com',
            css_class='event-info'
        )
        event_queryset = CalendarEvent.objects.filter(id=event.id)
        expected_json = '''{
            "result": [
                {
                    "end": "1394991000000",
                    "title": "Some Event Test",
                    "url": "http://example.com",
                    "id": 1,
                    "start": "1394973000000",
                    "class": "event-info"
                }
            ],
            "success": 1
        }'''
        self.assertJSONEqual(event_serializer(event_queryset), expected_json)
