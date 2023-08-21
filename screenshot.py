from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.by import By
from utils import Config

# Set the headless option.
class Screenshot:
    def __init__(self):
        opts = FirefoxOptions()
        opts.add_argument("--headless")
        self.driver = webdriver.Firefox(options=opts)

    def screenshot(self):
        self.driver.get("http://127.0.0.1:{}/quote/".format(Config.FLASK_RUN_PORT))
        
        if Config.RETURN_PNG:
            return self.driver.find_element(By.ID, "app").screenshot_as_png
        else:
            return self.driver.find_element(By.ID, "app").screenshot_as_base64