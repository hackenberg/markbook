from markbook.models import Note


def test_index(server):
    rv = server.get("/", follow_redirects=True)
    assert rv.status_code == 200
    assert "Notebook".encode("utf-8") in rv.data
    assert "close".encode("utf-8") in rv.data


def test_get_note(server, db):
    note = Note("TITLE", "TEXT")
    db.session.add(note)
    db.session.commit()
    rv = server.get("/notes/" + str(note.id), follow_redirects=True)
    assert rv.status_code == 200
    assert "<p>TEXT</p>".encode("utf-8") in rv.data
