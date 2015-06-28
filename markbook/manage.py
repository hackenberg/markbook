import sys
import webbrowser

from markbook import app, manager
from markbook.util import list_notes, open_note


@manager.command
def list():
    list_notes()


@manager.command
def open(note_title):
    open_note(note_title)


@manager.command
def notebook():
    webbrowser.open_new_tab("http://localhost:5000")
    app.run()


def main():
    manager.run()
