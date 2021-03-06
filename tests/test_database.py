from markbook.models import Note


def test_delete_note(session, db):
    note = Note("DELETE_TITLE", "DELETE_TEXT")
    db.session.add(note)
    db.session.commit()
    db.session.delete(note)
    db.session.commit()
    assert Note.query.get(note.id) is None


def test_insert_note(session, db):
    note = Note("INSERT_TITLE", "INSERT_TEXT")
    db.session.add(note)
    db.session.commit()
    result = Note.query.get(note.id)
    assert result.title == note.title
    assert result.text == note.text
    assert result.get_html() == note.get_html()


def test_repr_note():
    note = Note("DEFAULT_TITLE", "DEFAULT_TEXT")
    assert str(note) == "<Note DEFAULT_TITLE>"
