import xlrd
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

### Variable ####
username = '<Your TestRail username >';
password = '<Your TestRail password >';

workbook = xlrd.open_workbook("FunctionalTestCases.xlsx")
sheet = workbook.sheet_by_name("Sheet1")
driver = webdriver.Chrome(ChromeDriverManager().install())
rowCount = sheet.nrows;
colCount = sheet.ncols;
get_title_text_from_ui = '';

#### step definition ####
def goToTestRails():
    driver.get("https://cenergy.testrail.net/index.php?/suites/view/26621&group_by=cases:section_id&group_order=asc&display_deleted_cases=0&group_id=234690")

def login():
    driver.find_element("id", "name").send_keys("piyathida.sa@central.tech");
    driver.find_element("id", "password").send_keys("Zxcv@12141618");
    driver.find_element("id", "button_primary").click();

def click_title_link_and_click_edit():
    time.sleep(5)
    driver.find_element_by_link_text(title_from_excel).click();
    ## click Edit ###
    driver.find_element_by_xpath('//*[@id="content-header"]/div/div[3]/a[1]').click();

## step ##
goToTestRails();
login();

#### Get data from excel ###
for curr_row in range(1, rowCount):
    cardRef_from_excel = sheet.cell_value(curr_row,0);
    title_from_excel = sheet.cell_value(curr_row,1);

    print("total of row: " + str(rowCount))
    print("Row number: " + str(curr_row))
    print(title_from_excel)
    print(cardRef_from_excel)

    click_title_link_and_click_edit();
    check_reference_data =  driver.find_element_by_xpath('//*[@id="refs"]').get_attribute('value');
    
    if (check_reference_data == ''):
        get_title_text_from_ui = driver.find_element_by_xpath('//*[@id="content-header"]/div/div[4]').text;
        if(get_title_text_from_ui == title_from_excel):
            driver.find_element_by_xpath('//*[@id="refs"]').send_keys(cardRef_from_excel);
            time.sleep(5)
            driver.find_element_by_id('accept').click();
            time.sleep(15)
            goToTestRails();
        else:
            goToTestRails();
    else:   
        goToTestRails();
