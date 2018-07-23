import Event
import webapp2

class NewEventHandler(webapp2.RequestHandler):
    def get(self):
        new_event = Event.Event()
        new_event.title = 'Test Event'
        new_event.description = 'this is a test event.'
        new_event.tags = 'test, event'
        print "done!"
        new_event.put()

app = webapp2.WSGIApplication([
    ('/create', NewEventHandler)
], debug=True)
