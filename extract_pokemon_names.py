import json

input_file = 'pokemon_with_url.txt'
output_file = 'pokemon.txt'

error = False
new_records = []

# Best practice: Include comments close to code itself
"""    
    Open and read data file. Extract each chacter name while assigning it an ID
    :param str in_file: Name of file to be read
    :param str out_file: Name of file to be written to
"""
# Open and read data file. Extract each chacter name while assigning it an ID

def create_list_from_file(in_file, out_file):
    with open(in_file, 'r') as input:
        data = input.read()
        records = json.loads(data)
        with open(out_file, 'w') as output:
            id_num = 0
            for record in records:
                r = {}
                id_num += 1
                r['id'] = str(id_num)
                r['name'] = record['name']
                new_records.append(r)
            output.write(json.dumps(new_records, indent=2))

create_list_from_file(input_file, output_file)

