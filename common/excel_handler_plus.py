import openpyxl
from common.excel_handler import ExcelHandler


class ExcelHandlerPlus(ExcelHandler):
    def read_excel(self, sheet_name):
        sheet = self.open_excel(sheet_name)
        rows = sheet.rows


if __name__ == "__main__":
    exc = ExcelHandlerPlus('C:/Users/TUNGEE/Desktop/api_test_excel_template.xlsx')
    sheet = exc.open_excel('Sheet1')
    print(exc.get_columns('Sheet1'))
    rows = list(sheet.rows)
    cell = sheet.cell.row
    print('11')
