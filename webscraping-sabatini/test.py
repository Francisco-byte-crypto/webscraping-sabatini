from selenium.webdriver.support import expected_conditions as EC
from driver.create_web_driver import create_web_driver
from scraper.Page_Context import Page_Context
from scraper.Page_Content import Page_Content
from processing.clean_dataframe_data import clean_dataframe_data 
from selenium.webdriver.common.by import By

def _test_():
    driver, wait = create_web_driver()
    driver.get("https://www.hierrossabatini.com/#")
    driver.get("https://www.hierrossabatini.com/index.php")
    page = Page_Context(driver, wait)
    page.update_homepage_context()
    if(page.is_show_more_clicked()):
        pass
    else:
        page.click_show_more()
    page.update_homepage_context()

    list_length = page.get_list_length()
    page_content = Page_Content(driver, wait)
    count = 0
    for index in range(list_length):
        count = count + 1
        print(count)
        page.material_list_current_index = index
        page.materials_list[index].click()
        page_content.add_page_content()
        page.go_back()
        page.update_homepage_context()
        if(count==17): break
        

    df = clean_dataframe_data(page_content.get_page_dataframe())
    df.to_excel('excel.xlsx')
_test_()