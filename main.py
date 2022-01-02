import base64
import os.path as fp


GD_FILE_NAME = 'GeometryDash.exe'
CURRENT_SERVER = b''
DEFAULT_SERVER_URL = 'http://www.boomlings.com/database'
URL_LEN = len(DEFAULT_SERVER_URL)


def init():
    global CURRENT_SERVER
    with open(GD_FILE_NAME, mode='rb') as file:
        result = file.read()
        pos = result.find(b'/accounts/loginGJAccount.php')
        CURRENT_SERVER = result[slice(pos - URL_LEN, pos)]


def convert(server: bytes):
    old_enc_b64 = base64.b64encode(CURRENT_SERVER)
    b64 = base64.b64encode(server)

    with open(GD_FILE_NAME, mode='rb') as file:
        result = file.read() \
            .replace(CURRENT_SERVER, server) \
            .replace(old_enc_b64, b64)

    with open(GD_FILE_NAME, mode='wb') as file:
        file.write(result)


def main():
    if not fp.exists(GD_FILE_NAME):
        print(f"Файл {GD_FILE_NAME} не найден.")
        return
    init()

    print(f"Введите URL нужного сервера. Пример: {DEFAULT_SERVER_URL}")
    url = input("URL: ")

    if len(url) != URL_LEN:
        print("Ошибка! Адрес сервера имеет недействительную длину!")
        print(f"Адрес сервера должен иметь длину в {URL_LEN}. Текущая: {len(url)}")
        return
    convert(url.strip().encode('ascii'))

    print("Готово :3")
    input()


if __name__ == '__main__':
    main()
