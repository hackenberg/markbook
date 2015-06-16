from flask import jsonify, render_template, request

from markbook import app
from markbook.models import Note


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


# error handlers

@app.errorhandler(404)
def not_found(error):
    handle(404, "Not Found")


@app.errorhandler(500)
def internal_server_error(error):
    handle(500, "Internal Server Error")


def handle(code, message=None):
    error = dict(code=code, message=message)
    if request.json:
        return jsonify(error=error), code
    return render_template("error.html", error=error), code
