import markdown

from markbook import db


class Note(db.Model):

    __tablename__ = "notes"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    text = db.Column(db.String, nullable=False)

    def __init__(self, title, text):
        self.title = title
        self.text = text

    def __repr__(self):
        return "<Note {}>".format(self.title)

    def get_html(self):
        return markdown.markdown(self.text)
