"""This file is where we create flask app and its principals components."""

# flake8: noqa W293 E501

from flask import Flask, jsonify, request
from utils import load_data, assert_data_type, save_data, auto_increment_id
from flask_cors import CORS

app = Flask(__name__)
endpoint = '/api/v1'
DB_FILE_PATH = "db_objects.json"
CORS(app=app)


if __name__ == "__app__":
    app.run(debug=False)


@app.route(f'{endpoint}/list_objects/', methods=['GET'])
def list_objects():
    objects = load_data(DB_FILE_PATH)
    return jsonify(objects), 200


@app.route(f'{endpoint}/add_object/', methods=['POST'])
def save_object():
    try:
        new_object_data = request.get_json()
        new_object_data['id'] = auto_increment_id(DB_FILE_PATH)
        assert_data_type(new_object_data)
        objects = load_data(DB_FILE_PATH)
        objects.append(new_object_data)
        save_data(DB_FILE_PATH, objects)
        return jsonify(new_object_data), 201
    
    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500  # noaq: E501
    

@app.route(f'{endpoint}/update_object/', methods=['PUT'])
def update_object():
    try:
        updated_object_data = request.get_json()
        object_id = updated_object_data.get("id")

        if not object_id:
            return jsonify({"error": "ID is required to update an object"}), 400  # noaq: E501
        
        objects = load_data(DB_FILE_PATH)
        assert_data_type(updated_object_data)
        object_to_update = None
        for object in objects:
            if object["id"] == object_id:
                object_to_update = object
                break
        if object_to_update is None:
            return jsonify({"error": "Object not found"}), 404
        object_to_update.update(updated_object_data)

        save_data(DB_FILE_PATH, objects)

        return jsonify(object_to_update), 200

    except ValueError as ve:
        return jsonify({"error": str(ve)}), 400
    
    except Exception as e:
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500
    

@app.route(f'{endpoint}/delete_object/', methods=['DELETE'])
def delete_object():
    try:

        delete_object_data = request.get_json()
        object_id = delete_object_data.get("id") 

        if not object_id:
            return jsonify({"error": "ID is required to delete an object"}), 400
 
        objects = load_data(DB_FILE_PATH)

    
        object_to_delete = None
        for object in objects:
            if object["id"] == object_id:
                object_to_delete = object
                break
        
        if object_to_delete is None:
            return jsonify({"error": "Object not found"}), 404
        
        objects.remove(object_to_delete)

        save_data(DB_FILE_PATH, objects)

        return jsonify({"message": f"Object with ID {object_id} deleted successfully"}), 200

    except Exception as e:
        return jsonify({"error": "Internal Server Error", "message": str(e)}), 500