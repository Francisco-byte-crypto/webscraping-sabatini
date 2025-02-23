from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from driver.create_web_driver import create_web_driver
from scraper.Page_Context import Page_Context
from scraper.Page_Content import Page_Content
from processing.clean_dataframe_data import clean_dataframe_data 

def main():
    driver, wait = create_web_driver()
    page = Page_Context(driver, wait)
    page_content = Page_Content(driver, wait)
    driver.get("https://www.hierrossabatini.com/#")
    driver.get("https://www.hierrossabatini.com/index.php")
    page.update_homepage_context()
    
    if(page.is_show_more_clicked()):
        pass
    else:
        page.click_show_more()
    
    page.update_homepage_context()
    list_length = page.get_list_length()
    
    for index in range(list_length):
        page.material_list_current_index = index
        page.materials_list[index].click()
        page_content.add_page_content()
        page.go_back()
        page.update_homepage_context()
        if(page.material_list_current_index == 5): break

    dataframe = clean_dataframe_data(page_content.get_page_dataframe())
    dataframe.to_excel("./data/dataframe.xlsx")

main()