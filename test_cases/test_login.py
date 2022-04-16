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
        """
        账号正确
        密码正确
        鉴权正确
        """
        res = self.req.visit('post', url=self.login_url, data=self.payload, headers=self.header)
        self.assertEqual(200, res.status_code, 'status code error!')
        self.assertEqual(1, res.json()['stat'], 'sign in fail!')

    def test_phone_null(self):
        """
        账号为空
        密码正确
        鉴权正确
        """
        payload_phone = self.payload
        payload_phone['phone'] = ''
        payload_phone.update()
        res = self.req.visit('post', url=self.login_url, data=self.payload, headers=self.header)
        self.assertEqual(400, res.status_code, 'status code error!')
        self.assertEqual('Need image code', res.json()['msg'], 'sign in fail!')

    def test_password_null(self):
        """
        账号为空
        密码正确
        鉴权正确
        """
        res = self.req.visit('post', url=self.login_url, data=self.payload, headers=self.header)
        self.assertEqual(400, res.status_code, 'status code error!')


if __name__ == "__main__":
    unittest.main()
