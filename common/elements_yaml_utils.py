import yaml
import os

current_path = os.path.dirname(__file__)
yaml_date_path = os.path.join(current_path, '../element_info_data/element_infos_login_page.yaml')

def get_element_from_yaml(yaml_date_path):
    f=open(yaml_date_path,'r',encoding='utf-8')
    cfg=f.read()
    elements_data=yaml.load(cfg,Loader=yaml.FullLoader)
    return  elements_data


