from flask import render_template, request

from server import app
from server.models import Note


@app.route("/", methods=["GET"])
def index():
    notes = Note.query.order_by(Note.title)
    return render_template("index.html", notes=notes)


@app.route("/notes/<int:id>", methods=["GET"])
def get_note(id):
    note = Note.query.get(id)
    return render_template("note.html", note=note)


@app.route("/shutdown", methods=["GET", "POST"])
def shutdown():
    func = request.environ.get("werkzeug.server.shutdown")
    if func is None:
        raise RuntimeError("Not running with the Werkzeug Server")
    func()
    return "Server shutting down..."
