from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from utils import Config

class Screenshot:
    def __init__(self):
        # Set the headless option.
        opts = Options()
        opts.add_argument("--headless")
        if Config.GECKODRIVER_PATH:
            service = Service(executable_path=Config.GECKODRIVER_PATH)
            self.driver = webdriver.Firefox(options=opts, service=service)
        else:
            self.driver = webdriver.Firefox(options=opts)
            
    def __del__(self):
        if hasattr(self, 'driver'):
            self.driver.quit()

    def screenshot(self, ret_type, unique_id):
        self.driver.get(f"http://127.0.0.1:{Config.FLASK_RUN_PORT}/quote/?id={unique_id}")
        
        if ret_type == 'png':
            return self.driver.find_element(By.ID, "app").screenshot_as_png
        elif ret_type == 'base64':
            return self.driver.find_element(By.ID, "app").screenshot_as_base64