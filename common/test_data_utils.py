#!/usr/bin/env python
# encoding:utf-8
# @author: lvhuayan
# @file: test_data_utils.py
# @time: 2020/5/12 22:40
# @desc:

import os
from common.config_utils import local_config
from common.excel_utils import ExcelUtils

current_path=os.path.dirname(__file__)
test_data_path=os.path.join(current_path,'..',local_config.testdata_path,'test_data_infos.xlsx')


class TestDateUtils():
    def __init__(self,test_suitename,test_classname):
        self.test_classname=test_classname
        self.excel_data=ExcelUtils(test_suitename,test_data_path).get_all_data_by_list()
        self.excel_rows=ExcelUtils(test_suitename,test_data_path).get_row_count
    def convert_exceldata_to_testdata(self):
        # {'test_login_success':
        #      {'test_name':'验证是否能成功进行登录','isnot':'是','excepted_result':'测试人员1','test_parameter':{'username':'test01','password':'newdream123'} }
        #  'test_login_fail':
        #      { }
        #  }
        test_data_infos={}
        for i in range(1,self.excel_rows):
            test_data_info={}
            if self.excel_data[i][2].__eq__(self.test_classname):
                test_data_info['test_name']=self.excel_data[i][1]
                test_data_info['isnot'] = self.excel_data[i][3]
                test_data_info['expect_result'] = self.excel_data[i][4]
                test_parameter={}
                for j in range(5,len(self.excel_data[i])):
                    if self.excel_data[i][j].__contains__('=') and len(self.excel_data[i][j])>2:
                        parameter_info=self.excel_data[i][j].split('=')
                        test_parameter[parameter_info[0]]=parameter_info[1]
                    test_data_info['test_parameter']=test_parameter
                test_data_infos[self.excel_data[i][0]]=test_data_info
            return test_data_infos



if __name__=='__main__':
    value=TestDateUtils('login_suite','LoginTest').convert_exceldata_to_testdata()
    print(value)

