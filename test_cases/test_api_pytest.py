import platform

import ddt
import pytest
from common.logger_handler import logger
from common.request_handler import RequestHandler as rh
from common.excel_handler import ExcelHandler


@ddt.ddt
class TestAPIPytest:
    # initial case data
    if platform.system() == 'Windows':
        my_path = 'C:/Users/TUNGEE/Desktop/api_test_excel_template.xlsx'
    elif platform.system() == 'Mac':
        my_path = '/Users/chenyw/Desktop/小陈的工作做不完/learning/api_test_excel_template.xlsx'

    excel = ExcelHandler(my_path)
    case_data = excel.read_excel()

    @ddt.data(*case_data)
    def test_api(self, case):
        logger.info('start request')
        res = rh.visit(method=case['method'], url=case['url'], data=eval(case['payload']),
                       headers=eval(case['headers']))
        logger.debug(f'response: {res.json()}')
        # 缺少对比
