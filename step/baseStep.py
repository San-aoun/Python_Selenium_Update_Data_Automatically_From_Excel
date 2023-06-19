import xlrd
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from base.base_element import BaseElement
from helper.elementVariable import *
from helper.properties import *
from helper.wait_until import *

#### step definition ####
class BaseStep(BaseElement):
    def __init__(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        BaseElement.__init__(self, self.driver)

    def goToHomePage(self,url):
        self.driver.get(url)
            
    def login(self,username,password):
        self.type((By.ID, ele_login_page()['user']),username)
        self.type((By.ID, ele_login_page()['password']),password)
        self.click((By.ID, ele_login_page()['login_btn']))

    def update_testrail_from_excel(self):
        excel = xlrd.open_workbook(get_settings()['DEFAULT-EXCEL'])
        sheet = excel.sheet_by_name(get_settings()['DEFAULT-SHEET'])
        rowCount = sheet.nrows;

        for curr_row in range(1, rowCount):
            cardRef_from_excel = sheet.cell_value(curr_row,0);
            title_from_excel = sheet.cell_value(curr_row,1);
            testCaseId_from_excel = sheet.cell_value(curr_row,2);
            funtion_from_excel = sheet.cell_value(curr_row,3);
            feature_from_excel = sheet.cell_value(curr_row,4);
            step_from_excel = sheet.cell_value(curr_row,5);

            print("total of row: " + str(rowCount))
            print("Row number: " + str(curr_row))
            print(title_from_excel)
            print(cardRef_from_excel)

            tiltle_link_by_testCaseId = '//td[text()="' + testCaseId_from_excel +'"]/ancestor::tr/td/a/span[@class="title"]';
            self.click((By.XPATH, tiltle_link_by_testCaseId))
            self.click((By.XPATH, ele_edit_page()['edit_btn']))

            check_reference_data =  self.driver.find_element_by_xpath(ele_edit_page()['refs']).get_attribute('value');
            get_title_text_from_ui = self.driver.find_element_by_xpath(ele_edit_page()['titleUI']).text;
            
            if(get_title_text_from_ui == title_from_excel):
                if (check_reference_data == '' and cardRef_from_excel != ''):
                    self.type((By.XPATH,ele_edit_page()['refs']),cardRef_from_excel)
                
                if (funtion_from_excel != ''):
                    self.type((By.ID,ele_edit_page()['custom_function']),funtion_from_excel)
                
                if (feature_from_excel != ''):
                    self.type((By.ID,ele_edit_page()['custom_feature']),feature_from_excel)
                
                if (step_from_excel != ''):
                    self.type((By.ID,ele_edit_page()['custom_steps_display']),step_from_excel)
                
                self.click(((By.ID, 'accept')))

                wait_until_presence_of_element_located((By.XPATH, ele_edit_page()['successfully_message']))
                self.goToHomePage();
            else:
                self.goToHomePage();
