# Google Project Challenge - Shopping List
Simple webapp that provides users with an ability to keep track of a shopping list. 

The app is based on [Creating a Guestbook Application][1] tutorial by Google Cloud.

## What was used:
* Python 2.
* webapp2 framework.
* Jinja2 templates.
* Google App Engine.
* Google Cloud Platform.

## Supported Actions:
* add an item
* view the whole shopping list
* delete an item
* delete the entire shopping list with a single click
* login with a Google account

## How to use:
- Cloning the project from GitHub and running locally.

Install the [Google Cloud SDK][2] and initialize the `gcloud` tool.

`git clone https://github.com/yvlnv/google_project_challenge.git`

`cd google_project_challenge`

`dev_appserver.py ./`

Visit [http://localhost:8080/][3] in your web browser to view the app.

- Alternatively, you can access the app here: [https://shopping-list-270317.appspot.com/][4].

Note: you need to sing in with your Google Account in order to access the app.

## Things to Improve:
* Support using the app without having to log in.
* Support delete confirmation pop up when a user deletes an item or a shopping list.
* Support updating items.
* When all items are shown support 'hide all' action to show the last 10 items.

[1]: https://cloud.google.com/appengine/docs/standard/python/getting-started/creating-guestbook
[2]: https://cloud.google.com/appengine/docs/standard/python/download
[3]: http://localhost:8080/
[4]: https://shopping-list-270317.appspot.com/
