from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class Page_Context:
    
    def __init__(self, driver:object, wait: object, materials_navbar: object = None,
                materials_list: list = None, list_length: int = None, material_list_current_index: int = None,
                 show_more_clicked: bool = None
                ):
        self.driver = driver
        self.wait = wait
        self.materials_navbar = materials_navbar
        self.materials_list = materials_list
        self.list_length = list_length
        self.material_list_current_index = material_list_current_index
        self.show_more_clicked = show_more_clicked
            
    def update_homepage_context(self):
        MATERIALS_NAVBAR_ID = 'navbar'
        PRELOADER_ID = 'preloader'
        TAG_NAME = 'a'
        self.wait.until(EC.invisibility_of_element_located((By.ID, PRELOADER_ID))) # I don't know what this preloader is but if i don't wait for it to be invisible then it throws and exception.
        self.materials_navbar = self.wait.until(EC.visibility_of_element_located((By.ID, MATERIALS_NAVBAR_ID)))
        self.materials_list = self.materials_navbar.find_elements(By.TAG_NAME, TAG_NAME)
        self.materials_list.pop(-1) # We take off the last <a> since it's not important.

    def get_list_length(self):
        self.list_length = len(self.materials_list)
        return self.list_length
    
    def click_show_more(self):
        LINK_TEXT = 'VER MÁS'
        A_TAG = self.materials_navbar.find_element(By.LINK_TEXT, LINK_TEXT)
        A_TAG.click()

    def is_show_more_clicked(self):
        LINK_TEXT = 'VER MÁS'
        #EC.invisibility_of_element_located returns true in case it's invisible.
        show_more_invisible = EC.invisibility_of_element_located((By.LINK_TEXT, LINK_TEXT))(self.driver)
        if(show_more_invisible):
            self.show_more_clicked = True 
            return self.show_more_clicked
        
        else:
            self.show_more_clicked = False
            return self.show_more_clicked
    
    def go_back(self):
        self.driver.back()

    
