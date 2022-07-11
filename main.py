import requests
from pprint import pprint


class VK:

    def __init__(self, token, user_id, version='5.131'):
        self.token = access_token
        self.id = user_id
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}

    def get_photos(self):
        url = 'https://api.vk.com/method/photos.get'
        params = {'owner_id': self.id, 'extended': 1, 'album_id': 'profile'}
        response = requests.get(url, params={**self.params, **params})
        return response.json()
photo_url = 'https://sun9-88.userapi.com/c9591/u00001/136592355/w_818d6f79.jpg'

class YaUpLoader:
    def __init__(self, token: str):
        self.token = yandex_token

    def get_headers(self):
        return {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)}

    def upload(self, file_path, photo_url):
        url = 'https://cloud-api.yandex.net:443/v1/disk/resources/upload'
        headers = self.get_headers()
        params = {'path': file_path, 'url1' : photo_url}
        response = requests.get(url, headers=headers, params=params)
        return response.json()

    def upload_to_disk(self, file_path, photo_url):
        response_href = self.upload(file_path, photo_url)
        href = response_href.get('href', '')
        response_ = requests.put(href, data=photo_url)

        response_.raise_for_status()
        if response_.status_code == 201:
            print('Success')


with open('token.txt', 'r') as file_object:
    access_token = file_object.read().strip()
user_id = input('Введите id пользователя')
vk = VK(access_token, user_id)

with open('yandex_token.txt', 'r') as file_object:
    yandex_token = file_object.read().strip()
ya = YaUpLoader(yandex_token)
print(yandex_token)

dict_ = {}

photos = vk.get_photos()


def get_photo_url():
    for info in photos['response']['items']:
        base = 0
        big_photo = ''
        likes = info['likes']['count']
        for size in info['sizes']:
            if size['type'] == 'w':
                big_photo = size['url']
                base = 1

            elif size['type'] == 'z' and base != 1:
                big_photo = size['url']
                base = 2

            elif size['type'] == 'y' and base != 1 or 2:
                big_photo = size['url']
                base = 3

            elif size['type'] == 'r' and base != 1 or 2 or 3:
                big_photo = size['url']
                base = 4
            elif size['type'] == 'q' and base != 1 or 2 or 3 or 4:
                big_photo = size['url']
                base = 5

            elif size['type'] == 'p' and base != 1 or 2 or 3 or 4 or 5:
                big_photo = size['url']
                base = 6
            elif size['type'] == 'o' and base != 1 or 2 or 3 or 4 or 5 or 6:
                big_photo = size['url']
                base = 7
            elif size['type'] == 'x' and base != 1 or 2 or 3 or 4 or 5 or 6 or 7:
                big_photo = size['url']
                base = 8
            elif size['type'] == 'm' and base != 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8:
                big_photo = size['url']
                base = 9
            elif size['type'] == 's' and base != 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
                big_photo = size['url']

        dict_[likes] = big_photo


# pprint(photos)
get_photo_url()

pprint(dict_)
for photo in dict_:
    likes = str(photo)
    photo_url = dict_[photo]
    ya.upload_to_disk(file_path = 'photos/' + likes + '.jpg',photo_url = photo_url)
# print(photo_url)


# ya.upload_to_disk()
