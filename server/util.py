import markdown
import os
import tempfile

from server import db
from server.models import Note


def open_note(title):
    fd, path = tempfile.mkstemp(suffix=title)
    os.close(fd)
    note = Note.query.filter_by(title=title).first()
    if note:
        with open(path, "w") as f:
            f.write(note.text)
    os.system("vim " + path)
    with open(path, "r") as f:
        text = f.read()
    if note:
        note.text = text
        note.html = markdown.markdown(text)
    else:
        db.session.add(Note(title, text, markdown.markdown(text)))
    db.session.commit()
    os.unlink(path)
