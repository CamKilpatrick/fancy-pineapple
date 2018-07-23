import Event
import webapp2

import

class NewEventHandler(webapp2.RequestHandler):
    def get(self):
        new_event = Event.Event()
        new_event.eventname = self.request.get('eventname')
        new_event.description = self.request.get('description')
        new_event.tags = self.request.get('tags')
        new_event.start= self.request.get('start')
        new_event.end= self.request.get('end')
        new_event.location= self.request.get('location')
        print "Event Created!"
        new_event.put()

app = webapp2.WSGIApplication([
    ('/create', NewEventHandler)
], debug=True)
