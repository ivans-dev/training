# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest

class AddGroup(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome(r'D:\chromedriver')
        self.wd.implicitly_wait(30)

    
    def add_group(self):
        wd = self.wd
        self.open_main_page(wd)
        self.login(wd, login="admin", password="secret")
        self.create_group(wd, name="Test", header="Testing group", footer="Testing group")
        self.return_group_page(wd)
        self.logout(wd)

    def add_empty_group(self):
        wd = self.wd
        self.open_main_page(wd)
        self.login(wd, login="admin", password="secret")
        self.create_group(wd, name="", header="", footer="")
        self.return_group_page(wd)
        self.logout(wd)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def return_group_page(self, wd):
        wd.find_element_by_link_text("group page").click()

    def create_group(self, wd, name, header, footer):
        wd.find_element_by_link_text("groups").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(footer)
        wd.find_element_by_name("submit").click()

    def login(self, wd, login, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(login)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def open_main_page(self, wd):
        # переход на главную страницу и авторизация
        wd.get("http://localhost:8080/group.php")

    def is_element_present(self, how, what):
        try: self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.wd.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    
    def tearDown(self):
        self.wd.quit()

if __name__ == "__main__":
    unittest.main()
