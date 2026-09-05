"""
Intentionally vulnerable Flask app — a fixture for testing SAST scanning
(Opengrep) against real, findable weaknesses. Do not deploy. See README.md.
"""

import hashlib
import os
import pickle
import sqlite3

from flask import Flask, request

import config

app = Flask(__name__)


@app.route("/ping")
def ping():
    # CWE-78: OS command injection — host comes straight from the request
    # and is concatenated into a shell command.
    host = request.args.get("host", "")
    return os.popen(f"ping -c 1 {host}").read()


@app.route("/user")
def get_user():
    # CWE-89: SQL injection — user_id is spliced directly into the query.
    user_id = request.args.get("id", "")
    conn = sqlite3.connect("app.db")
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM users WHERE id = {user_id}")
    return str(cursor.fetchall())


@app.route("/load", methods=["POST"])
def load_object():
    # CWE-502: insecure deserialization of an untrusted request body.
    data = request.get_data()
    obj = pickle.loads(data)
    return str(obj)


@app.route("/file")
def read_file():
    # CWE-22: path traversal — filename comes from the request with no
    # sanitization before being joined onto the base directory.
    filename = request.args.get("name", "")
    path = os.path.join("/var/app/uploads", filename)
    with open(path) as f:
        return f.read()


def hash_password(password: str) -> str:
    # CWE-327: MD5 is not a suitable password hash.
    return hashlib.md5(password.encode()).hexdigest()


def get_db_connection_string() -> str:
    return f"postgresql://{config.DB_USER}:{config.DB_PASSWORD}@{config.DB_HOST}/app"


if __name__ == "__main__":
    app.run(debug=True)
