import xlrd
import os
from common.config_utils import local_config
from common.excel_utils import ExcelUtils

current_path = os.path.dirname(__file__)
element_data_excel = os.path.join(current_path, '../element_info_data/element_infos_data.xlsx')

class ElementDataUtils:
    def __init__(self,model_name,page_name):
        self.excel_utils=ExcelUtils(element_data_excel,model_name)
        self.page_name=page_name

    def get_element_info(self):
        elements_info={}
        for i in range(1,self.excel_utils.get_row_count):
            if self.excel_utils.sheet_data.cell_value(i, 2)==self.page_name:
                element_info={}
                element_info['element_name']=self.excel_utils.sheet_data.cell_value(i,1)
                element_info['locator_type'] = self.excel_utils.sheet_data.cell_value(i, 3)
                element_info['locator_value'] = self.excel_utils.sheet_data.cell_value(i, 4)
                timeout_value=self.excel_utils.sheet_data.cell_value(i, 5)
                element_info['timeout'] =timeout_value if isinstance(timeout_value,float) else local_config.time_out
                elements_info[self.excel_utils.sheet_data.cell_value(i,0)]=element_info
        return elements_info
if __name__=='__main__':
    elements=ElementDataUtils('login','login_page').get_element_info()
    for element in elements.values():
        print(element)


