import random
import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

PEOPLE = []


@app.route('/office/people', methods=['GET', 'POST'])
def all_people():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        PEOPLE.append({'id': uuid.uuid4().hex,
                       'name': request.get_json().get('name')})
        response_object['message'] = 'Person added!'
    else:
        response_object['people'] = PEOPLE
    return jsonify(response_object)


@app.route('/office/people/<person_id>', methods=['DELETE'])
def remove_person(person_id):
    response_object = {'status': 'success'}
    for person in PEOPLE:
        if person['id'] == person_id:
            PEOPLE.remove(person)
    response_object['message'] = 'Person removed!'
    return jsonify(response_object)


def generate_configuration():
    assignment = {}
    used_desks = random.sample(range(1, 12), len(PEOPLE))
    for (desk, person) in zip(used_desks, PEOPLE):
        assignment['desk' + str(desk)] = person['name']
    return assignment


@app.route('/office/randomize', methods=['GET'])
def randomize_desks():
    response_object = {'status': 'success'}
    assignment = generate_configuration()
    response_object['desks'] = assignment
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()