#!/usr/bin/env python3

import webbrowser

from markbook import app, db, manager
from markbook.util import open_note


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
