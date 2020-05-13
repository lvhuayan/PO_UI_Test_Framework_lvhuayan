import os
from configparser import ConfigParser

current_path=os.path.dirname(__file__)
config_path=os.path.join(current_path,'../conf/config.ini')


class ConfigUtils(object):
    def __init__(self,path=config_path):
        self.cfg=ConfigParser()
        self.cfg.read(path)
    @property
    def url(self):
        url_value=self.cfg.get('default','url')
        return url_value

    @property
    def driver_path(self):
        driver_path_value =self.cfg.get('default','driver_path')
        return driver_path_value

    @property
    def driver_name(self):
        driver_name_value =self.cfg.get('default','driver_name')
        return driver_name_value

    @property
    def time_out(self):
        time_out_value =float(self.cfg.get('default','time_out'))
        return time_out_value

    @property
    def screenshot_path(self):
        screenshot_path_value =self.cfg.get('default','screenshot_path')
        return screenshot_path_value

    @property
    def username(self):
        username_value =self.cfg.get('default','username')
        return username_value

    @property
    def password(self):
        password_value =self.cfg.get('default','password')
        return password_value

    @property
    def excel_path(self):
        excel_path_value =self.cfg.get('default','excel_path')
        return excel_path_value

    @property
    def log_path(self):
        log_path_value =self.cfg.get('default','log_path')
        return log_path_value

    @property
    def log_level(self):
        log_level_value =self.cfg.get('default','log_level')
        return log_level_value

    @property
    def testdata_path(self):
        testdata_path_value =self.cfg.get('default','testdata_path')
        return testdata_path_value

    @property
    def case_path(self):
        case_path_value =self.cfg.get('default','case_path')
        return case_path_value

    @property
    def report_path(self):
        report_path_value =self.cfg.get('default','report_path')
        return report_path_value

local_config=ConfigUtils()


if __name__=='__main__':
   config= ConfigUtils()
   print(config.report_path)
