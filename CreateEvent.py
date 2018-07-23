import Event

class NewEventHandler(webapp2.RequestHandler):
    def get(self):
        new_event = Event.Event()
        event.title = 'Test Event'
        event.description = 'this is a test event.'
        event.tags = 'test, event'
        })
        print "done!"
        console.log("done!")
        new_event.put()

app = webapp2.WSGIApplication([
    ('/create', NewEventHandler)
], debug=True)
