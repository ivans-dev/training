# -*- coding: utf-8 -*-
import unittest

from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import NoSuchElementException
from group import Group
from contact import Contact
from address import Address


class TestABook(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Chrome(r'D:\chromedriver')
        self.wd.implicitly_wait(30)

    def test_add_group(self):
        wd = self.wd
        self.open_main_page(wd)
        self.login(wd, login="admin", password="secret")
        self.create_group(wd, Group(name=u"Тестовая", header=u"Тестовая Header", footer=u"Тестовая  Footer"))
        self.return_group_page(wd)
        self.logout(wd)

    def test_add_empty_group(self):
        wd = self.wd
        self.open_main_page(wd)
        self.login(wd, login="admin", password="secret")
        self.create_group(wd, Group(name="", header="", footer=""))
        self.return_group_page(wd)
        self.logout(wd)
    def test_add_contact(self):
        wd = self.wd
        self.open_main_page(wd)
        self.login(wd, login="admin", password="secret")
        self.create_contact(wd)
        self.add_address(wd,Address(u"Российская Федерация, Тульская обалсть, г. Тула"))
        self.add_contact_info(wd, Contact(firstname="Иванов", lastname="Иван", middlename="Иванович", title="Менеджер"))
        self.get_main(wd)
        self.logout(wd)

    #Добавление информации о контакте
    def add_contact_info(self, wd,contact):
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("theform").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    #Добавление адреса при заполнении информации о контакте
    def add_address(self, wd, address):
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(address.address)
        wd.find_element_by_xpath("(//input[@name='quickadd'])[2]").click()

    #Переход на главную страницу
    def get_main(self, wd):
        wd.find_element_by_link_text(u"Главная").click()

    #Создание контакта
    def create_contact(self, wd):
        wd.find_element_by_link_text(u"Добавить контакт").click()

    #Выход
    def logout(self, wd):
        wd.find_element_by_link_text(u"Выйти").click()

    #Переход в группы
    def return_group_page(self, wd):
        wd.find_element_by_link_text("group page").click()

    # Создание группы
    def create_group(self, wd, group):
        wd.find_element_by_link_text(u"Группы").click()
        wd.find_element_by_name("new").click()
        wd.find_element_by_name("group_name").click()
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").click()
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        wd.find_element_by_name("submit").click()

    #Авторизация
    def login(self, wd, login, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(login)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath(u"//input[@value='Войти']").click()

    #Открытие главной страницы
    def open_main_page(self, wd):
        # переход на главную страницу
        wd.get("http://localhost:8080/")

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
