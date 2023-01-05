import requests
import json
from keys import my_apikey, my_hash

characters = requests.request(
  "GET",
  "http://gateway.marvel.com/v1/public/characters?ts=1&apikey={api1}&hash={hash1}"
  .format(api1=my_apikey, hash1=my_hash))
charactersJSON = characters.json()

numberOfPages = charactersJSON['data']['total'] / 100
print(numberOfPages)
offset = 0
Master_dict = {}
Master_dict_temp = {}
while numberOfPages > 0:
  people = requests.get(
    "http://gateway.marvel.com/v1/public/characters?ts=1&apikey={api1}&hash={hash1}&limit=100&offset={offset1}"
    .format(api1=my_apikey, hash1=my_hash, offset1=offset))
  peopleJSON = people.json()
  for chracter_id in peopleJSON["data"]["results"]:
    if 'image_not_available' not in str(chracter_id["thumbnail"]["path"]):

      Master_dict_temp[chracter_id['name']] = chracter_id["thumbnail"][
        "path"] + "/portrait_incredible.jpg"

  Master_dict.update(Master_dict_temp)

  offset = offset + 100
  numberOfPages = numberOfPages - 1
  Master_dict_temp = {}
