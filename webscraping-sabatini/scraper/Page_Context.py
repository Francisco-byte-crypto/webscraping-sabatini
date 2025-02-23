from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Page_Context:

    material_list_current_index: int
    show_more_clicked: bool
    materials_navbar: object
    materials_list: list
    list_length: int
    driver: object
    wait: object
    
    def __init__(self, driver=None, wait=None):
        self.driver = driver
        self.wait = wait
            
    def update_homepage_context(self):
        MATERIALS_NAVBAR_ID = 'navbar'
        TAG_NAME = 'a'
        self.wait.until(EC.invisibility_of_element_located((By.ID, "preloader"))) # I don't know what this preloader is but if i don't wait for it to be invisible then it throws and exception.
        self.materials_navbar = self.wait.until(EC.visibility_of_element_located((By.ID, MATERIALS_NAVBAR_ID)))
        self.materials_list = self.materials_navbar.find_elements(By.TAG_NAME, TAG_NAME)
        self.materials_list.pop(-1) # We take off the last <a> since it's not important.

    def get_list_length(self):
        self.list_length = len(self.materials_list)
        return self.list_length
    
    def click_show_more(self):
        A_TAG = self.materials_navbar.find_element(By.LINK_TEXT, 'VER MÁS')
        A_TAG.click()

    def is_show_more_clicked(self):
        #EC.invisibility_of_element_located returns true in case it's invisible.
        show_more_invisible = EC.invisibility_of_element_located((By.LINK_TEXT, 'VER MÁS'))(self.driver)
        if(show_more_invisible):
            self.show_more_clicked = True 
            return self.show_more_clicked
        
        else:
            self.show_more_clicked = False
            return self.show_more_clicked
    
    def go_back(self):
        self.driver.back()

    