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


def check_availability():
    """"""
    return len(PEOPLE) < 11


def add_person_office(name):
    """"""
    PEOPLE.append({'id': uuid.uuid4().hex,
                   'name': name})
    return f"{name} is succesvol toegevoegd!"


def add_person_single(name):
    """"""
    available_desks = list(range(1, 12))
    for person in PEOPLE:
        available_desks.remove(person['desk'])
    new_person = {'id': uuid.uuid4().hex,
                  'name': name,
                  'desk': random.choice(available_desks)}
    PEOPLE.append(new_person)
    return f"{name} is succesvol toegevoegd!"


def get_desk_assignment():
    assignment = {}
    for person in PEOPLE:
        if 'desk' in person:
            assignment['desk' + str(person['desk'])] = person['name']
    return assignment


@app.route('/office/people', methods=['GET', 'POST'])
def all_people():
    if request.method == 'POST':
        if check_availability():
            response_object = {'status': "success"}
            if request.get_json().get('mode') == "office":
                response_object['message'] = add_person_office(request.get_json().get('name'))
            elif request.get_json().get('mode') == "single":
                response_object['message'] = add_person_single(request.get_json().get('name'))
                response_object['desks'] = get_desk_assignment()
        else:
            response_object = {'status': "failure",
                               'message': "Maximale capaciteit bereikt!"}
    else:
        response_object = {'status': "success",
                           'people': PEOPLE,
                           'desks': get_desk_assignment()}
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
    used_desks = random.sample(range(1, 12), len(PEOPLE))
    for (desk, index) in zip(used_desks, range(len(PEOPLE))):
        person = PEOPLE[index]
        person['desk'] = desk
        PEOPLE[index] = person


@app.route('/office/randomize', methods=['GET'])
def randomize_desks():
    response_object = {'status': 'success'}
    generate_configuration()
    return jsonify(response_object)


@app.route('/office/reset', methods=['GET'])
def reset():
    response_object = {'status': 'success'}
    PEOPLE.clear()
    response_object['message'] = 'Reset complete!'
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()