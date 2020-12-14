# -*- coding: utf-8 -*-
import unittest

from address import Address
from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from contact import Contact
from group import Group
from add_contact import TestContact
from add_group import TestGroup


class TestABook(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome(r'D:\chromedriver')
        self.wd.implicitly_wait(30)

    def test_add_group(self):
        wd = self.wd
        TestGroup.open_main_page(wd)
        TestGroup.login(wd, login="admin", password="secret")
        TestGroup.create_group(wd, Group(name=u"Тестовая", header=u"Тестовая Header", footer=u"Тестовая  Footer"))
        TestGroup.return_group_page(wd)
        TestGroup.logout(wd)

    def test_add_empty_group(self):
        wd = self.wd
        TestGroup.open_main_page(wd)
        TestGroup.login(wd, login="admin", password="secret")
        TestGroup.create_group(wd, Group(name="", header="", footer=""))
        TestGroup.return_group_page(wd)
        TestGroup.logout(wd)

    def test_contact(self):
        wd = self.wd
        TestContact.open_main_page(wd)
        TestContact.login(wd, login="admin", password="secret")
        TestContact.create_contact(wd)
        TestContact.add_address(wd, Address(u"Российская Федерация, Тульская обалсть, г. Тула"))
        TestContact.add_contact_info(wd, Contact(firstname="Иванов", lastname="Иван", middlename="Иванович", title="Менеджер"))
        TestContact.get_main(wd)
        TestContact.logout(wd)

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
