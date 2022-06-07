from flask import Flask, jsonify, redirect, url_for, make_response
import json
# Best Practice: Use of tested libraries for code functionality

app = Flask(__name__)

# Future functionality would involve passing <path>/file or loading data from a database
# Best Practice: Use meaningful names for variables, reducing the need to over-comment code
input_file = 'pokemon.txt'

# Best Practice: DRY - Don't repeeat yourself
# Modularize code for reuse to minimize code redundancy
# and the posibility of errors

# Best Practice: Keep comments brief but succinct
# Best Practice: Comment function use and required parameters
"""    
    Return input_file contents
    :param str input_file: Name of file to be read
    :return: the message id
    :rtype: list
"""
def read_file(input_file):
    with open(input_file, 'r') as data_file:
        data = data_file.read()
        file_list = json.loads(data)
        return file_list

@app.route('/')
def index():
    return redirect(url_for('pokemon'))

@app.route('/api/v1/pokemon', methods=['GET'])
@app.route('/pokemon', methods=['GET'])
def pokemon():
    error = False
    response = {}
    try:
        file_data = read_file(input_file)
        response = {
            'count': len(file_data),
            'results': file_data
        }
    except:
        error = True
    if error:
        message = jsonify({'Error': 'Internal Server Error.'})
        return make_response(message, 500)
    else:
        return jsonify(response)


@app.route('/api/v1/pokemon/<id>', methods=['GET'])
@app.route('/pokemon/<id>', methods=['GET'])
def get_pokemon_by_id(id):
    error = False
    record_found = False
    pokemon_by_id = {}
    try:
        file_data = read_file(input_file)
        for pokemon in file_data:
            if pokemon['id'] == id:
                record_found = True
                pokemon_by_id = pokemon
    except:
        error = True
    if error:
        message = jsonify({'Error': 'Internal server error.'})
        return make_response(message, 500)
    elif not record_found:
        message = jsonify({'Error': 'ID not found.'})
        return make_response(message, 404)   
    else:    
        return jsonify(pokemon_by_id)

if __name__ == '__main__':
    app.run()

# Best Practice: Create tests subfolder and use to perform unit testing
# Best Practice: Support error handling to avoid crashes
# Best Practice: Include relevant info in readme file.