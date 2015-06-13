from flask import Blueprint, jsonify

from markbook.models import Note


api = Blueprint('api', __name__)


@api.route('/api', methods=["GET"])
def api_routes():
    versions = {
        "v1": {
            "notes_url": "http://localhost:5000/api/v1/notes/"
        }
    }
    return jsonify({"versions": versions})


@api.route("/api/v1/notes", methods=["GET"])
def api_notes():
    url = "http://localhost:5000/api/v1/notes/{}"
    results = Note.query.order_by(Note.id)
    notes = [url.format(note.id) for note in results]
    meta = {
        "total": results.count()
    }
    return jsonify({"notes": notes, "meta": meta})


@api.route("/api/v1/notes/<int:id>", methods=["GET"])
def api_get_note(id):
    result = Note.query.get(id)
    note = {
        "title": result.title,
        "text": result.text,
    }
    return jsonify({"note": note})
