from selenium.webdriver.common.by import By
from .base_tracker import BaseTracker

class CathoderaytubeTracker(BaseTracker):
    def __init__(self, driver, config):
        self.tracker_name = "cathode-raytube"
        super().__init__(driver, config, self.tracker_name)

    def login(self):
        super().login(login_url=self.config[self.tracker_name]["login_url"])

    def click_login_button(self):
        login_button = self.driver.find_element(By.CLASS_NAME, "submit")
        login_button.click()

    def take_screenshot(self, tracker_name, is_load_at_runtime=False):
        super().take_screenshot(self.tracker_name)

    def run(self):
        super().run()