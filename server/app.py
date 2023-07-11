import random
import uuid

from flask import Flask, jsonify, request
from flask_cors import CORS


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True
    }
]

PEOPLE = [
    {'id': uuid.uuid4().hex,
     'name': "Ruben"
    },
    {'id': uuid.uuid4().hex,
     'name': "Luc"
    },
    {'id': uuid.uuid4().hex,
     'name': "Walter"
    }
]


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


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
    print(assignment)
    return jsonify(response_object)


@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)


def remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False


@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(book_id)
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read')
        })
        response_object['message'] = 'Book updated!'
    if request.method == 'DELETE':
        remove_book(book_id)
        response_object['message'] = 'Book removed!'
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()