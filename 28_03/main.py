import requests
from requests.auth import HTTPBasicAuth, HTTPDigestAuth

BASE_URL = "https://httpbin.org"
USERNAME = "user123"
PASSWORD = "password_secret"
TOKEN = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IlBvbHlha292IE1heGltIiwiYWRtaW4iOnRydWUsImlhdCI6MTUxNjIzOTAyMn0.1abigoNbXXzjuIQswuPx6FyfCGpNN65-wORVMsd2zgc"

def test_basic_auth():
    print("--- 1. Basic Auth ---")
    # Эндпоинт ожидает совпадения данных в URL и в заголовках
    url = f"{BASE_URL}/basic-auth/{USERNAME}/{PASSWORD}"
    
    # Можно передать кортежем: auth=(user, pass)
    response = requests.get(url, auth=(USERNAME, PASSWORD))
    
    if response.status_code == 200:
        print("Успех:", response.json().get("authenticated"))
    else:
        print(f"Ошибка: {response.status_code}")
    print()

def test_bearer_auth():
    print("--- 2. Bearer Token Auth ---")
    url = f"{BASE_URL}/bearer"
    
    # Bearer передается вручную через словарь headers
    headers = {
        "Authorization": f"Bearer {TOKEN}",
        "Accept": "application/json"
    }
    
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        print("Токен принят:", response.json().get("token"))
    else:
        print(f"Ошибка: {response.status_code}")
    print()

def test_digest_auth():
    print("--- 3. Digest Auth ---")
    # Алгоритм: /digest-auth/{qop}/{user}/{passwd}
    # qop (quality of protection) обычно ставим 'auth'
    url = f"{BASE_URL}/digest-auth/auth/{USERNAME}/{PASSWORD}"
    
    # Для Digest обязательно используем специальный объект
    response = requests.get(url, auth=HTTPDigestAuth(USERNAME, PASSWORD))
    
    if response.status_code == 200:
        print("Успех:", response.json().get("authenticated"))
    else:
        print(f"Ошибка: {response.status_code}")
    print()

if __name__ == "__main__":
    try:
        test_basic_auth()
        test_bearer_auth()
        test_digest_auth()
    except requests.exceptions.RequestException as e:
        print(f"Проблема с соединением: {e}")