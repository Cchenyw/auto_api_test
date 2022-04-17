import unittest
from common.request_handler import RequestHandler


class LoginTest(unittest.TestCase):

    def setUp(self) -> None:
        self.req = RequestHandler()
        """init var"""
        self.login_url = 'https://user.tungee.com/api/individual-user/login'
        self.payload = {
            'phone': '17520544566',
            'password': '69b77fe60044a9706bddd58cd37373d6',
            'remember': 0,
            'code': '',
            'area_code': '86'
        }
        self.header = {
            # 'Content-Type': 'multipart/form-data',
            'Referer': 'https://user.tungee.com/users/sign-in',
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36'
        }

    def tearDown(self) -> None:
        self.req.close_session()

    def test_login_success(self):
        """账号正确 密码正确 请求头正确"""
        res = self.req.visit('post', url=self.login_url, data=self.payload, headers=self.header)
        self.assertEqual(200, res.status_code, f'status code error!\n{res.json()}')
        self.assertEqual(1, res.json()['stat'], 'sign in fail!')

    def test_phone_null(self):
        """账号为空 密码正确 请求头正确"""
        payload_phone_null = self.payload
        payload_phone_null['phone'] = ''
        res = self.req.visit('post', url=self.login_url, data=payload_phone_null, headers=self.header)
        self.assertEqual(400, res.status_code, 'status code error!')
        self.assertEqual('Account or pwd error', res.json()['msg'], 'return msg is error')

    def test_password_null(self):
        """账号正确 密码为空 请求头正确"""
        payload_password_null = self.payload
        payload_password_null['password'] = ''
        res = self.req.visit('post', url=self.login_url, data=payload_password_null, headers=self.header)
        self.assertEqual(400, res.status_code, 'status code error!')
        self.assertEqual('Account or pwd error', res.json()['msg'], 'return msg is error')

    def test_header_wrong(self):
        """账号正确 密码为空 请求头正确"""
        header_wrong = self.header
        header_wrong['password'] = ''
        res = self.req.visit('post', url=self.login_url, data=self.payload, headers=self.header)
        self.assertEqual(412, res.status_code, 'status code error!')
        self.assertEqual('Forbidden', res.json()['msg'], 'return msg is error')
        self.assertEqual(0, res.json()['stat'], 'return stat is error')


if __name__ == "__main__":
    unittest.main()
