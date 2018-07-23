from google.appengine.ext import ndb

class Event(ndb.Model):
    title = ndb.StringProperty(required=True)
    description = ndb.StringProperty(required=True)
    tags = ndb.StringProperty(required=True)
