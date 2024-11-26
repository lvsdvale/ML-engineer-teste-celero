"""This file is where we create flask app and its principals components."""

from flask import Flask, jsonify
from utils import load_data

app = Flask(__name__)
endpoint = '/api/v1'
DB_FILE_PATH = "db_objects.json"


@app.route(f'{endpoint}/list_objects/', methods=['GET'])
def list_objects():
    objects = load_data(DB_FILE_PATH)
    return jsonify(objects), 200
