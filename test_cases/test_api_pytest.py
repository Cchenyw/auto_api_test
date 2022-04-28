import platform

import pytest
from common.logger_handler import logger
from common.request_handler import RequestHandler
from common.excel_handler import ExcelHandler
from common.string_handler import StringHandler as sh


class TestAPIPytest:
    # initial case data
    if platform.system() == 'Windows':
        my_path = 'C:/Users/TUNGEE/Desktop/api_test_excel_template.xlsx'
    elif platform.system() == 'Darwin':
        my_path = '/Users/chenyw/Desktop/小陈的工作做不完/learning/api_test_excel_template.xlsx'

    excel = ExcelHandler(my_path)
    case_data = excel.read_excel('Sheet1')

    @pytest.mark.parametrize("items", case_data)
    def test_api(self, items):
        # log
        logger.info('*' * 88)
        logger.info(f'当前是第{items["case_id"]}条用例：{items["case_title"]}')
        logger.info(f'当前测试数据：{items}')
        logger.info('start request')
        rh = RequestHandler()
        res = rh.visit(method=items['method'], url=items['url'], data=eval(items['payload']),
                       headers=eval(items['headers']))
        logger.debug(f'response: {res.json()}')
        rh.close_session()

        # 数据比对
        try:
            expected_kws = sh(eval(items['expected'])).get_key_word_list()
            result_kws = sh(res.json()).get_key_word_list()
            # 不严格校验，只校验格式
            for ex_re in zip(expected_kws, result_kws):
                assert ex_re[0]['key'] == ex_re[1]['key']
            result = 'pass'
            logger.info(f'{res.json()}')
            logger.info(f'test-result: {result}')
        except AssertionError as e:
            result = 'fail'
            logger.error(f'用例执行失败，{e}')
            raise e
        finally:
            TestAPIPytest.excel.write_excel(file=self.my_path,
                                            sheet_name='Sheet1', row=items['case_id'] + 1, column=9,
                                            data=res.status_code)
            TestAPIPytest.excel.write_excel(file=self.my_path,
                                            sheet_name='Sheet1', row=items['case_id'] + 1, column=10,
                                            data=result)
            logger.info('The result has been written to excel')


if __name__ == "__main__":
    pytest.main()
