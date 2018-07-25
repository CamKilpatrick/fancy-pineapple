import webapp2
import random
import datetime
import jinja2
import os
from google.appengine.ext import ndb
from login import LoginHandler



jinja_env = jinja2.Environment(
    loader= jinja2.FileSystemLoader(os.path.dirname(__file__)),
)

def SearchByName(name):
    newsearch = Event.query().filter(Event.eventnamelower==name.lower())
    return newsearch


def SearchByTag(tagname):
    if tagname=="theatertag":
        newsearch = Event.query().filter(Event.theatertag=="on")
        return newsearch
    elif tagname=="musictag":
        newsearch = Event.query().filter(Event.musictag=="on")
        return newsearch
    elif tagname=="dancetag":
        newsearch = Event.query().filter(Event.dancetag=="on")
        return newsearch
    else:
        pass


def DateTimeConverter(timestring):
    s = datetime.datetime.strptime(timestring, "%Y-%m-%dT%H:%M")
    return s

class Event(ndb.Model):
    eventname = ndb.StringProperty(required=True)
    eventnamelower = ndb.StringProperty(required=True)
    description = ndb.StringProperty(required=True)
    musictag = ndb.StringProperty(required=True)
    dancetag = ndb.StringProperty(required=True)
    theatertag = ndb.StringProperty(required=True)
    end = ndb.DateTimeProperty(required=True)
    start =ndb.DateTimeProperty(required=True)
    location = ndb.StringProperty(required=True)

class MainPageHandler(webapp2.RequestHandler):
    def get(self):
        main_template = jinja_env.get_template('mp.html')
        html = main_template.render()
        self.response.write(html)



class FindEventsHandler(webapp2.RequestHandler):
    def get(self):
        findevents_template = jinja_env.get_template('fe.html')
        html = findevents_template.render()
        self.response.write(html)

class ActiveSearchHandler(webapp2.RequestHandler):
    def get(self):
        search = SearchByName(self.request.get("search_input"))
        search_iter = search.iter()
        if search_iter is not None:
           event_template = jinja_env.get_template('sr.html')
           html = event_template.render({
           'navigation': search_iter
           })
           self.response.write(html)
        else:
            self.response.write("Sorry, your seach turned up empty.")


#class TheaterSearchHandler(webapp2.RequestHandler):
#    def get(self):
#        search3 = SearchByTag("theatertag")
#        search4 = search3.get()
#        self.response.write(search4)
#        'events':
#        theater_template = jinja_env.get_template('/tagsearch.html')
#
#        html = theater_template.render({
#            'people': all_people,
#        })


class TheaterSearchHandler(webapp2.RequestHandler):
    def get(self):
        search3 = SearchByTag("theatertag")

        theater_template = jinja_env.get_template('/sr.html')
        ########### getting rid of tagsearch.
        html = theater_template.render({
            'navigation': search3.iter(),
            # 'blank': blank.blank,

                        # 'events': search3,
            # 'event_title': search3.eventname,
            # 'event_description': search3.description,
                        ##'tags': specific_event1.musictag
        })
        if search3_iter is not None:
            self.response.write(html)
        else:
            self.response.write("Sorry, your seach turned up empty.")

# search4 = search3.iter()
# self.response.write(search4)


class MusicSearchHandler(webapp2.RequestHandler):
    def get(self):
        search3 = SearchByTag("musictag")
        # search4 = search3.get()
        # self.response.write(search4)

class DanceSearchHandler(webapp2.RequestHandler):
    def get(self):
        search3 = SearchByTag("dancetag")
        # search4 = search3.get()
        # self.response.write(search4)

        #search3 = SearchByTag("musictag")
        #search4 = search3.get()
        #self.response.write(search4)


class EventTemplateHandler(webapp2.RequestHandler):
    def get(self):
        createvent_template= jinja_env.get_template('ce.html')
        html= createvent_template.render()
        self.response.write(html)

class NewEventHandler(webapp2.RequestHandler):
    def get(self):
        new_event = Event()
        myevent_template= jinja_env.get_template('myevent.html')
        html= myevent_template.render()
        self.response.write(html)
        new_event.eventnamelower = self.request.get('eventname').lower()
        new_event.eventname = self.request.get('eventname')
        new_event.description = self.request.get('description')
        new_event.musictag = self.request.get('musictag')
        new_event.theatertag = self.request.get('theatertag')
        new_event.dancetag = self.request.get('dancetag')
        new_event.start = DateTimeConverter(self.request.get('start'))
        new_event.end = DateTimeConverter(self.request.get('end'))
        new_event.location = self.request.get('location')
        new_event.put()

class EventHandler(webapp2.RequestHandler):
    def get(self, name):
        specific_event = Event.query().filter(Event.eventnamelower==name)
        specific_event1 = specific_event.get()
        event_template = jinja_env.get_template('ed.html')
        html = event_template.render({
        'event_title': specific_event1.eventname,
        'event_description': specific_event1.description,
        'tags': specific_event1.musictag,
        })
        self.response.write(html)

app = webapp2.WSGIApplication([
    ('/', MainPageHandler),
    ('/find', FindEventsHandler),
    ('/new', NewEventHandler),
    ('/create', EventTemplateHandler),
    ('/active', ActiveSearchHandler),
    ('/login', LoginHandler),
    ('/create', EventTemplateHandler),
    ('/login', LoginHandler),
    ('/create', EventTemplateHandler),
    ('/active', ActiveSearchHandler),
    ('/ED', EventHandler),
    ('/theater', TheaterSearchHandler),
    ('/music', MusicSearchHandler),
    ('/dance', DanceSearchHandler),
    ('/ed', EventHandler),
],debug=True)
