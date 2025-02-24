import sys
from io import BytesIO
from geocoder import get_ll_spn
import requests
from PIL import Image

# python полный_поиск.py Москва, ул. Ак. Королева, 12
toponym_to_find = " ".join(sys.argv[1:])

geocoder_api_server = "http://geocode-maps.yandex.ru/1.x/"

geocoder_params = {
    "apikey": "8013b162-6b42-4997-9691-77b7074026e0",
    "geocode": toponym_to_find,
    "format": "json"}

response = requests.get(geocoder_api_server, params=geocoder_params)
if not response:
    pass

json_response = response.json()
toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
ll, spn = get_ll_spn(toponym)

apikey = "496b2eb5-7eaa-4a9e-8b0a-2c74a238a856"
kord = toponym['Point']['pos'].split()
marker = f"{kord[0]},{kord[1]},pm2ywl"
map_params = {
    "ll": ll,
    "spn": spn,
    "apikey": apikey,
    "pt": marker
}

map_api_server = "https://static-maps.yandex.ru/v1"
response = requests.get(map_api_server, params=map_params)
im = BytesIO(response.content)
opened_image = Image.open(im)
opened_image.show()