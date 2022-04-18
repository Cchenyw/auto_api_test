import json
import platform
import unittest

import ddt

from common.request_handler import RequestHandler
from common.excel_handler import ExcelHandler


@ddt.ddt
class TestLoginDdt(unittest.TestCase):
    if platform.system() == 'Windows':
        my_path = 'C:/Users/TUNGEE/Desktop/api_test_excel_template.xlsx'
    elif platform.system() == 'Mac':
        my_path = '/Users/chenyw/Desktop/小陈的工作做不完/learning/api_test_excel_template.xlsx'

    excel = ExcelHandler(my_path)
    case_data = excel.read_excel('Sheet1')
    print(case_data)

    def setUp(self) -> None:
        self.req = RequestHandler()
        self.my_path = TestLoginDdt.my_path

    def tearDown(self) -> None:
        self.req.close_session()

    @ddt.data(*case_data)
    def test_login_success(self, items):
        res = self.req.visit(method=items['method'], url=items['url'], data=eval(items['payload']),
                             headers=eval(items['headers']))
        try:
            self.assertEqual(res.status_code, items['expected'])
            result = 'pass'
        except AssertionError as e:
            result = 'fail'
            raise e
        finally:
            TestLoginDdt.excel.write_excel(file=self.my_path,
                                           sheet_name='Sheet1', row=items['case_id'] + 1, column=9,
                                           data=res.status_code)
            TestLoginDdt.excel.write_excel(file=self.my_path,
                                           sheet_name='Sheet1', row=items['case_id'] + 1, column=10,
                                           data=result)


if __name__ == "__main__":
    unittest.main(verbosity=2)
