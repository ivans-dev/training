class TestGroup:

    #Переход в группы
    def return_group_page(wd):
        wd.find_element_by_link_text("group page").click()

    # Создание группы
    def create_group(wd, group):
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
    def login(wd, login, password):
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(login)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath(u"//input[@value='Войти']").click()

    #Открытие главной страницы
    def open_main_page(wd):
        # переход на главную страницу
        wd.get("http://localhost:8080/")

        # Выход
    def logout(wd):
         wd.find_element_by_link_text(u"Выйти").click()
