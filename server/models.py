from server import db


class Note(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, unique=True, nullable=False)
    text = db.Column(db.String, nullable=False)
    html = db.Column(db.String, nullable=False)

    def __init__(self, title, text, html):
        self.title = title
        self.text = text
        self.html = html

    def __repr__(self):
        return "<Note {}>".format(self.title)
