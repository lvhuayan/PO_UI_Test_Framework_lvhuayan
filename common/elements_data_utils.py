import xlrd
import os

current_path = os.path.dirname(__file__)
element_data_excel = os.path.join(current_path, '../element_info_data/element_infos_data.xlsx')

class ElementDataUtils:
    def __init__(self,page_name,date_path=element_data_excel):
        self.workbook=xlrd.open_workbook(date_path)
        self.sheet=self.workbook.sheet_by_name(page_name)
        self.rows=self.sheet.nrows

    def get_element_info(self):
        elements_info={}
        for i in range(1,self.rows):
            element_info={}
            element_info['element_name']=self.sheet.cell_value(i,1)
            element_info['locator_type'] = self.sheet.cell_value(i, 2)
            element_info['locator_value'] = self.sheet.cell_value(i, 3)
            element_info['timeout'] = self.sheet.cell_value(i, 4)
            elements_info[self.sheet.cell_value(i,0)]=element_info
        return elements_info
if __name__=='__main__':
    elements=ElementDataUtils('login_page').get_element_info()
    print(elements)

