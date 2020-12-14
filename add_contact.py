# -*- coding: utf-8 -*-
class TestContact:

    def add_contact_info(wd, contact):
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

    def add_address(wd, address):
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(address.address)
        wd.find_element_by_xpath("(//input[@name='quickadd'])[2]").click()


    def get_main(wd):
         wd.find_element_by_link_text(u"Главная").click()

        # Создание контакта
    def create_contact(wd):
         wd.find_element_by_link_text(u"Добавить контакт").click()

        # Выход
    def logout(wd):
         wd.find_element_by_link_text(u"Выйти").click()

    #Авторизация
    def login(wd, login, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(login)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath(u"//input[@value='Войти']").click()

    #Открытие главной страницы
    def open_main_page( wd):
        # переход на главную страницу
        wd.get("http://localhost:8080/")
