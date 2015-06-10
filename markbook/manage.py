#!/usr/bin/env python3

import webbrowser

from flask_script import Manager

from markbook import app, db
from markbook.util import open_note


manager = Manager(app)


@manager.command
def init():
    db.create_all()


@manager.command
def on(note_title):
    open_note(note_title)


@manager.command
def notebook():
    webbrowser.open_new_tab("http://localhost:5000")
    app.run()


def main():
    manager.run()
