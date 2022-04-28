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

    @pytest.mark.parametrize("case", case_data)
    def test_api(self, case):
        # log
        logger.info('*' * 88)
        logger.info(f'当前是第{case["case_id"]}条用例：{case["case_title"]}')
        logger.info(f'当前测试数据：{case}')
        logger.info('start request')
        rh = RequestHandler()
        res = rh.visit(method=case['method'], url=case['url'], data=eval(case['payload']),
                       headers=eval(case['headers']))
        logger.debug(f'response: {res.json()}')
        rh.close_session()

        # 数据比对
        try:
            expected_kws = sh(eval(case['expected'])).get_key_word_list()
            result_kws = sh(res.json()).get_key_word_list()
            # 不严格校验，只校验格式
            for ex_re in zip(expected_kws, result_kws):
                assert ex_re[0]['key'] == ex_re[1]['key']
                assert ex_re[0]['r_path'] == ex_re[1]['r_path']
                # 严格校验，校验格式和值
                # assert ex_re[0]['value'] == ex_re[1]['value']
            result = 'pass'
            logger.info(f'{res.json()}')
            logger.info(f'test-result: {result}')
        except AssertionError as e:
            result = 'fail'
            logger.error(f'用例执行失败，{e}')
            # raise e
        finally:
            TestAPIPytest.excel.write_excel(file=self.my_path,
                                            sheet_name='Sheet1', row=case['case_id'] + 1, column=9,
                                            data=res.status_code)
            TestAPIPytest.excel.write_excel(file=self.my_path,
                                            sheet_name='Sheet1', row=case['case_id'] + 1, column=10,
                                            data=result)
            logger.info('The result has been written to excel')


if __name__ == "__main__":
    # -q: output sample info
    # -m: run case who was marked
    # -x: stop after fail case
    # -s: output debug info like print
    # -v: output more info about test
    # -lf: run the fail case from the previous time
    pytest.main()
