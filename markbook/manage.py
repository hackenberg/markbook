import sys
import webbrowser

from alembic.util import CommandError
from flask_migrate import MigrateCommand

from markbook import app, manager
from markbook.util import open_note


manager.add_command("db", MigrateCommand)


@manager.command
def on(note_title):
    open_note(note_title)


@manager.command
def notebook():
    webbrowser.open_new_tab("http://localhost:5000")
    app.run()


def main():
    try:
        manager.run()
    except CommandError as e:
        print(e, file=sys.stderr)
