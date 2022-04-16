import requests


class RequestHandler:
    def __init__(self):
        """init a session object"""
        self.session = requests.session()

    def visit(self, method, url, params=None, data=None, json=None, headers=None, **kwargs):
        return self.session.request(method, url, params=params, data=data, json=json, headers=headers, **kwargs)

    def close_session(self):
        """close session"""
        self.session.close()


if __name__ == "__main__":
    test_rh = RequestHandler()
    payload = {
        'phone': '17520544566',
        'password': '69b77fe60044a9706bddd58cd37373d6',
        'remember': 0,
        'code': '',
        'area_code': '86'
    }
    header = {
        # 'Content-Type': 'multipart/form-data',
        'Referer': 'https://user.tungee.com/users/sign-in',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'
    }
    res = test_rh.visit('post', 'https://user.tungee.com/api/individual-user/login', data=payload, headers=header)
    print(res.text)
