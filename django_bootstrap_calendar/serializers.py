# -*- coding: utf-8 -*-
__author__ = 'sandlbn'

from django.db.models.query import QuerySet
import json


def event_serializer(events):
    """
    Serialize event model.

    :param events: A QuerySet of CalendarEvent
    :return: List of events in json format
    """
    objects_body = []

    if isinstance(events, QuerySet):
        for event in events:
            field = {
                "id": event.pk,
                "title": event.title,
                "url": event.url,
                "class": event.css_class,
                "start": event.start_timestamp,
                "end": event.end_timestamp
            }
            objects_body.append(field)

    objects_head = {
        "success": 1,
        "result": objects_body
    }
    return json.dumps(objects_head)
