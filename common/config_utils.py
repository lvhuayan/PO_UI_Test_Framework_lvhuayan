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

local_config=ConfigUtils()

if __name__=='__main__':
   config= ConfigUtils()
   print(config.url )
