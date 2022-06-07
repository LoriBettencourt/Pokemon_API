# Pokemon_Bett

Pokemon API allowing developers to access information about the Pokemon universe

### Get all pokemon names

GET /pokemon
GET /api/v1/pokemon

Returns:
{
  "count": 150, 
  "results": [
    {
      "id": "1", 
      "name": "bulbasaur"
    }, 
    {
      "id": "2", 
      "name": "ivysaur"
    }, 
    ...
    ...
    {
      "id": "150", 
      "name": "mewtwo"
    }
  ]
}

### Get pokemon by id

GET /pokemon/<id>
GET /api/v1/pokemon/<id>

Returns (for example):
{
  "id": "3", 
  "name": "venusaur"
}

### Setup

`python>3.7` required

### How to run?

python3 main.py

### Run the tests
From main project folder: 
python3 -m unittest tests/test_api.py
python3 -m unittest tests/test_api_by_id