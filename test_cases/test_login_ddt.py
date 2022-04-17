import json
import unittest

import ddt

from common.request_handler import RequestHandler
from common.excel_handler import ExcelHandler


@ddt.ddt
class TestLoginDdt(unittest.TestCase):
    excel = ExcelHandler('/Users/chenyw/Desktop/小陈的工作做不完/learning/api_test_excel_template.xlsx')
    case_data = excel.read_excel('Sheet1')
    print(case_data)

    def setUp(self) -> None:
        self.req = RequestHandler()

    def tearDown(self) -> None:
        self.req.close_session()

    @ddt.data(*case_data)
    def test_login_success(self, items):
        res = self.req.visit(method=items['method'], url=items['url'], data=items['payload'],
                             headers=items['header'])  # excel表缺一个header字段
        try:
            self.assertEqual(res.status_code, items['expect'][0])
            result = 'pass'
        except AssertionError as e:
            result = 'fail'
            raise e
        finally:
            TestLoginDdt.excel.write_excel(file='/Users/chenyw/Desktop/小陈的工作做不完/learning/api_test_excel_template.xlsx',
                                           sheet_name='Sheet1', row=items['case_id'] + 1, column=9,
                                           data=res.status_code)
            TestLoginDdt.excel.write_excel(file='/Users/chenyw/Desktop/小陈的工作做不完/learning/api_test_excel_template.xlsx',
                                           sheet_name='Sheet1', row=items['case_id'] + 1, column=10,
                                           data=result)


if __name__ == "__main__":
    unittest.main(verbosity=2)
