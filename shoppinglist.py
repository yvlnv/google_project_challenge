#!/usr/bin/env python

# [START imports]
import os
import urllib

from google.appengine.api import users
from google.appengine.ext import ndb

import jinja2
import webapp2

JINJA_ENVIRONMENT = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)
# [END imports]


def shoppinglist_key(user_email):
    """Constructs a Datastore key for a Shopping List entity.
    We use user email address as the key.
    """
    return ndb.Key('Username', user_email)


# [START item]
class User(ndb.Model):
    """Sub model for representing an user."""
    email = ndb.StringProperty(indexed=False)
    identity = ndb.StringProperty(indexed=False)


class Item(ndb.Model):
    """A main model for representing an individual Shopping List item."""
    user = ndb.StructuredProperty(User)
    content = ndb.StringProperty(indexed=False)
    date = ndb.DateTimeProperty(auto_now_add=True)
# [END item]


# [START main_page]
class MainPage(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()
        user_email = user.email()

        items_query = Item.query(ancestor=shoppinglist_key(user_email)).order(-Item.date)
        items = items_query.fetch(10)[::-1]

        url = users.create_logout_url(self.request.uri)
        url_linktext = 'Logout'

        template_values = {
            'items': items,
            'user': user,
            'url': url,
            'url_linktext': url_linktext,
            'user_email': user_email,
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))
# [END main_page]


# [START additem]
class AddItem(webapp2.RequestHandler):

    def post(self):
        user_email = users.get_current_user().email()
        item = Item(parent=shoppinglist_key(user_email))
        item.user = User(
                    identity=users.get_current_user().user_id(),
                    email=users.get_current_user().email())
        item.content = self.request.get('content')
        if len(item.content) > 0:
            item.put()

        self.redirect('/')
# [END additem]


# [START showall]
class ShowAll(webapp2.RequestHandler):

    def get(self):
        user = users.get_current_user()
        user_email = users.get_current_user().email()

        items_query = Item.query(ancestor=shoppinglist_key(user_email)).order(Item.date)
        items = items_query.fetch()

        url = users.create_logout_url(self.request.uri)
        url_linktext = 'Logout'

        template_values = {
            'items': items,
            'user': user,
            'url': url,
            'url_linktext': url_linktext,
            'user_email': user_email,
        }

        template = JINJA_ENVIRONMENT.get_template('index.html')
        self.response.write(template.render(template_values))
# [END showall]


# [START deleteitem]
class DeleteItem(webapp2.RequestHandler):

    def post(self):
        safe_key = self.request.get('k')
        key = ndb.Key(urlsafe=safe_key)
        key.delete()

        self.redirect('/')
# [END deleteitem]


# [START deleteall]
class DeleteAll(webapp2.RequestHandler):

    def post(self):
        user_email = users.get_current_user().email()
        items_query = Item.query(ancestor=shoppinglist_key(user_email)).fetch(keys_only=True)
        ndb.delete_multi(items_query)

        self.redirect('/')
# [END deleteall]


# [START app]
app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/additem', AddItem),
    ('/showall', ShowAll),
    ('/deleteitem', DeleteItem),
    ('/deleteall', DeleteAll),
], debug=True)
# [END app]