#!/usr/bin/env python
# encoding:utf-8
# @author: lvhuayan
# @file: runner_all_cases.py
# @time: 2020/5/13 17:35
# @desc:

import os
import unittest
from common import HTMLTestReportCN
from common.config_utils import local_config

current_path = os.path.abspath(os.path.dirname(__file__))
case_path = os.path.join( current_path , '..' , local_config.case_path )
report_path = os.path.join( current_path , '..' , local_config.report_path )

class RunAllCases:
    def __init__(self):
        self.test_case_path = case_path
        self.report_path = report_path
        self.title = '禅道自动化测试报告'
        self.description = '禅道测试'

    def run(self):
        discover = unittest.defaultTestLoader.discover(start_dir = self.test_case_path,
                                                       pattern='*_test.py',
                                                       top_level_dir=self.test_case_path)
        all_suite = unittest.TestSuite()
        all_suite.addTest(discover)

        report_dir = HTMLTestReportCN.ReportDirectory(self.report_path)
        report_dir.create_dir(self.title)
        report_path = HTMLTestReportCN.GlobalMsg.get_value('report_path')
        fp = open(report_path,'wb')
        runner = HTMLTestReportCN.HTMLTestRunner(stream=fp,
                                                 title=self.title,
                                                 description=self.description,
                                                 tester='吕华艳')
        runner.run(all_suite)
        fp.close()

if __name__ == '__main__':
    RunAllCases().run()