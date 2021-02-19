from selenium import webdriver
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper
import pytest


class Application:
    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox(r'D:\geckodriver')
        elif browser == "chrome":
            capabilities = {
                "browserName": 'chrome',
                "enableVNC": True,
                "enableVideo": True,
                "acceptSslCerts": True,
            }
            self.wd = webdriver.Remote(command_executor=f'http://192.168.88.242:4444/wd/hub', desired_capabilities=capabilities)
            self.wd.set_window_size(1920, 1080)
            self.wd.implicitly_wait(10)

        elif browser == "ie":
            self.wd = webdriver.Chrome(r'D:\IEDriverServer')
        else:
            raise ValueError("Unrecognized browser %s" % browser)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url = base_url

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False
