import requests
import json
#
# """
# making a json? dictionary for myself
# """
# isabella = """
#     {
#         "name": "Isabella Tang",
#         "height": "4ft 10in",
#         "hair_color":"black",
#         "eye_color":"brown",
#         "gender":"female",
#         "homeworld":"earth",
#         "schools":["YCIS","Keys School","Alto International","Kehillah"]
#     }
# """
# print(type(isabella)) ##isabella is string
#
# data = json.loads(isabella)##these are dictionaries
# print(type(data),data)

def get_person(n):
    """
    return a dictionary from star wars api from person
    """
    response = requests.get('http://swapi.co/api/people/%s/' % n) ## this is a requests.models.response
    row = response.text
    data = json.loads(row)
    return data['name']
