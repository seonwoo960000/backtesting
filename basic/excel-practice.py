import os

import pandas as pd

excel_base_path = f'{os.getcwd()}/excel'


def initialize():
    # for errors: open excel file and click save
    excel_path = os.path.join(excel_base_path, 'example1.xlsx')
    sheet_nme = 'sheet_name'
    excel = pd.read_excel(excel_path, sheet_name=sheet_nme)
    print(excel)


def main():
    initialize()


if __name__ == '__main__':
    main()
