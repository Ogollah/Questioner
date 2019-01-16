""""
This file stores details of the rsvp.
"""

RVSPS=[]

class Rsvp():
    class_count = 1
    def __init__(self):
        self.meetup_id = None
        self.topic = None
        self.status = None
        self.rsvp_id = Rsvp.class_count
        self.user_id = None
        Rsvp.class_count +=1

    def __repr__(self):
        return "Rsvp '{}'".format(self.status)