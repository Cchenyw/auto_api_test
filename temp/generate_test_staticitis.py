import platform
import sys

import pandas as pd
import openpyxl

init_data = {
    'case_id': [1],
    'model_name': ['model name'],
    'url': ['api url which prepare to test'],
    'headers': ['request\'s headers'],
    'case_title': ['case title'],
    'method': ['request method, get/post/put/delete...'],
    'payload': ['request data or params'],
    'expected': ['expect result'],
    'actual': ['actual result'],
    'test_result': ['test result']
}
if platform.system() == 'Windows':
    my_path = 'C:/Users/TUNGEE/Desktop/api_test_excel_template.xlsx'
elif platform.system() == 'Darwin':
    my_path = '/Users/chenyw/Desktop/小陈的工作做不完/learning/api_test_excel_template.xlsx'
df = pd.DataFrame(init_data)
df.to_excel(my_path, index=False)
print(df)
