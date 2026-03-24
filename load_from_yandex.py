from functools import cache
import ymaps

geocode = ymaps.Geocode('83f3ea4e-ddde-4e72-ba29-c50b86ca2a3b')

@cache
def get_addr(coords):
    response = geocode.reverse(coords)
    d = response['response']['GeoObjectCollection']['featureMember'][0]['GeoObject']['metaDataProperty']['GeocoderMetaData']['Address']['Components']
    
    return {
        di['kind']: di['name'] for di in d
    }

with open('required_to_load.txt', 'r') as f:
    required = f.read().splitlines()


print(get_addr("(30.437269358566127, 59.907543849777774)"))