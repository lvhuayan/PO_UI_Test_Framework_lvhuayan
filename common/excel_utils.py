#!/usr/bin/env python
# encoding:utf-8
# @author: lvhuayan
# @file: excel_utils.py
# @time: 2020/5/11 22:37
# @desc:

import xlrd
import os
from common.config_utils import local_config

current_path=os.path.dirname(__file__)
excel_value_path=os.path.join(current_path,'..',local_config.excel_path)
print(excel_value_path)

class ExcelUtils():
    def __init__(self,sheet_name=None,excel_path=excel_value_path):
        self.excel_path=excel_path
        self.sheet_name = sheet_name
        self.sheet_data=self.__get_sheet_data()

    def __get_sheet_data(self):
        workbook=xlrd.open_workbook(self.excel_path)
        if self.sheet_name:
            sheet=workbook.sheet_by_name(self.sheet_name)
        else:
            sheet = workbook.sheet_by_index(0)
        return sheet

    @property
    def get_row_count(self):
        row_count=self.sheet_data.nrows
        return row_count

    @property
    def get_col_count(self):
        col_count=self.sheet_data.ncols
        return col_count

    def get_all_data_by_list(self):
        all_data=[]
        for row in range(1,self.get_row_count):
            row_data=[]
            for col in range(self.get_col_count):
                row_cell_value=self.sheet_data.cell_value(row,col)
                row_data.append(row_cell_value)
            all_data.append(row_data)
        return all_data

if __name__=='__main__':
    Excel_utils=ExcelUtils('login')
    value=Excel_utils.get_all_data_by_list()
    print(value)




