import requests
import json


class Users:

    def register_user(self, username, email, password):

        headers = {"Content-type": "application/json"}
        payload = {
                "username": username,
                "email": email,
                "password": password
                }
        r = requests.post("http://107.170.43.69:8080/users",
                data=json.dumps(payload),
                headers=headers)

        return r.text


if __name__ == "__main__":
    print(Users().register_user("cruor", "kliknes@gmail.com", "password123"))
