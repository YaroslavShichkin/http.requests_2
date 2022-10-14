import requests

class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def get_headers(self):
        return {'Content-type': 'application/json',
                'Authorization': f'OAuth {self.token}'}

    def upload(self, file_path: str):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = self.get_headers()
        params = {'path': file_path, 'overwrite' : 'true'}
        response = requests.get(url, headers = headers, params = params)
        response = response.json()
        href = response.get('href', '')
        result = requests.put(href, data=open('text.txt', 'rb'))



if __name__ == '__main__':
    path_to_file = 'text.txt'
    token = input('Введите токен:')
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file)