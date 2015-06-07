import os
import unittest
import tempfile

import server
from server.models import Note


class DatabaseTestCase(unittest.TestCase):

    def setUp(self):
        self.db_fd, self.db_path = tempfile.mkstemp()
        server.app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + self.db_path
        server.app.config["TESTING"] = True
        self.app = server.app.test_client()
        self.db = server.db
        self.db.create_all()

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()
        os.close(self.db_fd)
        os.unlink(self.db_path)

    def test_delete_note(self):
        note = Note("DELETE_TITLE", "DELETE_TEXT", "DELETE_HTML")
        self.db.session.add(note)
        self.db.session.commit()
        self.db.session.delete(note)
        self.db.session.commit()
        self.assertIsNone(Note.query.get(note.id))

    def test_insert_note(self):
        note = Note("INSERT_TITLE", "INSERT_TEXT", "INSERT_HTML")
        self.db.session.add(note)
        self.db.session.commit()
        result = Note.query.get(note.id)
        self.assertEqual(result.title, note.title)
        self.assertEqual(result.text, note.text)
        self.assertEqual(result.html, note.html)


if __name__ == "__main__":
    unittest.main()
