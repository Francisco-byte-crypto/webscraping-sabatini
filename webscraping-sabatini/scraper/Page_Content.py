from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas

class Page_Content:
    
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait
        self.content_dictionary = {'producto': [], 'precio': []}
        self.content_dataframe = pandas.DataFrame
        pass

    def add_page_content(self):
        TABLE_ID = 'example'
        table = self.wait.until(EC.visibility_of_element_located((By.ID, TABLE_ID)))
        cells = table.find_elements(By.TAG_NAME, 'h4')
        CELLS_LENGTH = len(cells) 
        
        for i in range(0, CELLS_LENGTH, 2):
            # What we do here is grab the products in tuples of two trough each iteration.
            product_name = cells[i].text
            product_price = cells[i+1].text
            self.content_dictionary['producto'].append(product_name)
            self.content_dictionary['precio'].append(product_price)

    def get_page_dataframe(self):
        dataframe = pandas.DataFrame(data=self.content_dictionary)
        return dataframe
