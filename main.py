import pyotp
import time

# Чтение секретных ключей и их номеров из файла
def read_secret_keys(filename):
    secret_keys = []
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split(',')
                key_num = int(parts[0])
                secret_key = parts[1]
                secret_keys.append((key_num, secret_key))
    return secret_keys

# Генерация и сохранение TOTP-кодов в файлы
def generate_totp_codes(secret_keys):
    while True:
        for key_num, secret_key in secret_keys:
            totp = pyotp.TOTP(secret_key)
            totp_code = totp.now()
            filename = f"{str(key_num).zfill(2)}.txt"
            with open(filename, 'w') as file:
                file.write(totp_code)
            print(f"Обновлен файл '{filename}' с TOTP-кодом: {totp_code}")
        time.sleep(5)

# Путь к файлу с секретными ключами
secret_keys_file = 'secret_keys.txt'

# Чтение секретных ключей и их номеров из файла
secret_keys = read_secret_keys(secret_keys_file)

# Генерация и обновление TOTP-кодов в файлы каждые 5 секунд
generate_totp_codes(secret_keys)