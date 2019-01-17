"""
This file holds meetup model to store meetup details.
"""

import datetime

MEETUPS = []
class Meetup():
    class_count = 1
    def __init__(self):
        self.topic = None
        self.images = None
        self.description = None
        self.happeningOn = None
        self.createdOn = None
        self.Tags = None
        self.host = None
        self.hostFrom = None
        self.meetup_id = Meetup.class_count
        Meetup.class_count += 1

    def __repr__(self):
        return "Meetup '{}'>".format(self.topic)

