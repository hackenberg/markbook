from markbook.models import Note


def test_delete_note(server, db):
    note = Note("DELETE_TITLE", "DELETE_TEXT", "DELETE_HTML")
    db.session.add(note)
    db.session.commit()
    db.session.delete(note)
    db.session.commit()
    assert Note.query.get(note.id) is None


def test_insert_note(server, db):
    note = Note("INSERT_TITLE", "INSERT_TEXT", "INSERT_HTML")
    db.session.add(note)
    db.session.commit()
    result = Note.query.get(note.id)
    assert result.title == note.title
    assert result.text == note.text
    assert result.html == note.html
