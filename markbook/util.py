import os
import tempfile

from markbook import db
from markbook.models import Note


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
    else:
        db.session.add(Note(title, text))
    db.session.commit()
    os.unlink(path)
