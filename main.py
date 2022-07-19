import requests
from pprint import pprint
from tqdm import tqdm


class VK:

    def __init__(self, token, user_id, version='5.131'):
        self.token = access_token
        self.id = user_id
        self.version = version
        self.params = {'access_token': self.token, 'v': self.version}

    def get_photos(self):
        url = 'https://api.vk.com/method/photos.get'
        params = {'owner_id': self.id, 'extended': 1, 'album_id': 'profile', 'count':5}
        response = requests.get(url, params={**self.params, **params})
        return response.json()


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
        params = {'path': file_path, 'url1': photo_url, 'overwrite': 'true'}

        response = requests.get(url, headers=headers, params=params)
        return response.json()

    def upload_to_disk(self, file_path, photo_url):
        response_href = self.upload(file_path, photo_url)
        href = response_href.get('href', '')
        requests.put(href, data=open(photo_url, 'rb'))

    def create_folder(self, path):
        URL = 'https://cloud-api.yandex.net/v1/disk/resources'
        headers = self.get_headers()
        requests.put(f'{URL}?path={path}', headers=headers)


with open('token.txt', 'r') as file_object:
    access_token = file_object.read().strip()
user_id = input('Введите id пользователя')
vk = VK(access_token, user_id)

yandex_token = input('Введите яндекс токен: ')
ya = YaUpLoader(yandex_token)


url_dict = {}
likes_ = []
size_and_like_dict = {}
final_file = []
photos = vk.get_photos()
repeatable_likes = []


for lala in photos['response']['items']:
    likes_.append(lala['likes']['count'])
for like in likes_:
    if likes_.count(like) != 1:
        repeatable_likes.append(str(like))


def get_photo_url():
    for info in photos['response']['items']:
        base = 0
        date = str(info['date'])
        big_photo = ''
        size_ = ''
        likes = str(info['likes']['count'])

        for size in info['sizes']:
            if size['type'] == 'w':
                big_photo = size['url']
                base = 1
                size_ = size['type']

            elif size['type'] == 'z' and base != 1:
                big_photo = size['url']
                base = 2
                size_ = size['type']

            elif size['type'] == 'y' and base != 1 or 2:
                big_photo = size['url']
                base = 3
                size_ = size['type']

            elif size['type'] == 'r' and base != 1 or 2 or 3:
                big_photo = size['url']
                base = 4
                size_ = size['type']
            elif size['type'] == 'q' and base != 1 or 2 or 3 or 4:
                big_photo = size['url']
                base = 5
                size_ = size['type']

            elif size['type'] == 'p' and base != 1 or 2 or 3 or 4 or 5:
                big_photo = size['url']
                base = 6
                size_ = size['type']
            elif size['type'] == 'o' and base != 1 or 2 or 3 or 4 or 5 or 6:
                big_photo = size['url']
                base = 7
                size_ = size['type']
            elif size['type'] == 'x' and base != 1 or 2 or 3 or 4 or 5 or 6 or 7:
                big_photo = size['url']
                base = 8
                size_ = size['type']
            elif size['type'] == 'm' and base != 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8:
                big_photo = size['url']
                base = 9
                size_ = size['type']
            elif size['type'] == 's' and base != 1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9:
                big_photo = size['url']
                size_ = size['type']

        size_and_like_dict['filename'] = likes + 'jpg'
        size_and_like_dict['size'] = size_

        final_file.append(size_and_like_dict)

        if likes in repeatable_likes:
            url_dict[likes + '_' + date] = big_photo

        else:
            url_dict[likes] = big_photo


path = 'course_project_photos'
ya.create_folder(path)
get_photo_url()

pprint(final_file)
images = []

for filename in url_dict:
    image = url_dict[filename]
    api = requests.get(image)

    with open(f'photos/{filename}.jpg', 'wb') as file:
        file.write(api.content)
        images.append(filename + '.jpg')

for image_ in tqdm(images):
    file_path = f'photos\\{image_}'
    ya.upload_to_disk(file_path=f'{path}/' + image_, photo_url=file_path)
