import requests


class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str):
        url = "https://cloud-api.yandex.net/v1/disk/resources/upload"
        headers = {"Authorization": f"OAuth {self.token}"}
        params = {"path": file_path, "overwrite": "true"}
        response = requests.get(url, headers=headers, params=params)
        upload_url = response.json()["href"]

        with open(file_path, "rb") as file:
            files = {"file": file}
            response = requests.put(upload_url, files=files)

        if response.status_code == 201:
            print("Успешно!!!")
        else:
            print("Ошибка")


if __name__ == '__main__':
    path_to_file = input("Введите путь к файлу на компьютере: ")
    token = input("Введите ваш токен : ")

    uploader = YaUploader(token)
    uploader.upload(path_to_file)
