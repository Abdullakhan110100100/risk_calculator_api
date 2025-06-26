from functools import wraps
from flask import request, jsonify

VALID_TOKENS = {"supersecrettoken123"}

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.headers.get("Authorization", "")
        if not auth.startswith("Bearer "):
            return jsonify({"error": "Invalid auth header"}), 401

        token = auth.split(" ")[1]
        if token not in VALID_TOKENS:
            return jsonify({"error": "Unauthorized"}), 401

        return f(*args, **kwargs)
    return decorated
