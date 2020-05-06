import xlrd
import os
from common.config_utils import local_config

current_path = os.path.dirname(__file__)
element_data_excel = os.path.join(current_path, '../element_info_data/element_infos_data.xlsx')

class ElementDataUtils:
    def __init__(self,model_name,page_name,date_path=element_data_excel):
        self.workbook=xlrd.open_workbook(date_path)
        self.sheet=self.workbook.sheet_by_name(model_name)
        self.page_name=page_name
        self.rows=self.sheet.nrows

    def get_element_info(self):
        elements_info={}
        for i in range(1,self.rows):
            if self.sheet.cell_value(i, 2)==self.page_name:
                element_info={}
                element_info['element_name']=self.sheet.cell_value(i,1)
                element_info['locator_type'] = self.sheet.cell_value(i, 3)
                element_info['locator_value'] = self.sheet.cell_value(i, 4)
                timeout_value=self.sheet.cell_value(i, 5)
                element_info['timeout'] =timeout_value if isinstance(timeout_value,float) else local_config.time_out
                elements_info[self.sheet.cell_value(i,0)]=element_info
        return elements_info
if __name__=='__main__':
    elements=ElementDataUtils('login','login_page').get_element_info()
    for element in elements.values():
        print(element)


