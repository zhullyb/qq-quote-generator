from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from utils import Config

# Set the headless option.
class Screenshot:
    def __init__(self):
        opts = Options()
        opts.add_argument("--headless")
        if Config.GECKODRIVER_PATH:
            service = Service(executable_path='/root/geckodriver')
            self.driver = webdriver.Firefox(options=opts, service=service)
        else:
            self.driver = webdriver.Firefox(options=opts)

    def screenshot(self):
        self.driver.get("http://127.0.0.1:{}/quote/".format(Config.FLASK_RUN_PORT))
        
        if Config.RETURN_PNG:
            return self.driver.find_element(By.ID, "app").screenshot_as_png
        else:
            return self.driver.find_element(By.ID, "app").screenshot_as_base64