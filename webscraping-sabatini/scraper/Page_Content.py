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
        TAG_NAME = 'h4'
        table = self.wait.until(EC.visibility_of_element_located((By.ID, TABLE_ID)))
        cells = table.find_elements(By.TAG_NAME, 'TAG_NAME')
        CELLS_LENGTH = len(cells)
        
        START=0
        STOP=CELLS_LENGTH
        STEP=2
        for i in range(START, STOP, STEP):
            # What we do here is grab the products in pairs through each iteration.
            product_name = cells[i].text
            product_price = cells[i+1].text
            self.content_dictionary['producto'].append(product_name)
            self.content_dictionary['precio'].append(product_price)

    def get_page_dataframe(self):
        dataframe = pandas.DataFrame(data=self.content_dictionary)
        return dataframe
