from model.contact import Contact


class ContactHelper:
    def __init__(self, app):
        self.app = app

    def add(self, contact):
        wd = self.app.wd
        self.contact_page()
        wd.find_element_by_link_text("add new").click()
        self.contact_element(contact)
        wd.find_element_by_name("theform").click()
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.return_main_page()
        self.contact_cache = None

    def select_contact_by_index(self, index):
        wd = self.app.wd
        self.contact_page()
        wd.find_elements_by_name("selected[]")[index].click()

    def delete_first(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        wd.switch_to.alert.accept()
        self.return_main_page()
        self.contact_cache = None

    def edit_first(self):
        self.modify_contact_by_index(0)

    def modify_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.select_contact_by_index(index)
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.contact_element(contact)
        wd.find_element_by_name("update").click()
        self.return_main_page()
        self.contact_cache = None

    def contact_element(self, contact):
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        self.change_field_value("address", contact.address)
        self.change_field_value("company", contact.company)
        self.change_field_value("title", contact.title)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("email", contact.mail)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def contact_page(self):
        wd = self.app.wd
        if not len(wd.find_elements_by_xpath("//input[@value='Send e-Mail']")) > 0:
            wd.find_element_by_link_text("home").click()

    def return_main_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contacts_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.contact_page()
            self.contact_cache = []
            i = int(wd.find_element_by_id("search_count").text)
            j = 2
            x = 0
            while x != i:
                ids = wd.find_element_by_xpath(
                    "/html/body/div/div[4]/form[2]/table/tbody/tr[" + str(j) + "]/td[1]").find_element_by_name(
                    "selected[]").get_attribute("value")
                lastname = wd.find_element_by_xpath(
                    "/html/body/div/div[4]/form[2]/table/tbody/tr[" + str(j) + "]/td[2]").text
                firstname = wd.find_element_by_xpath(
                    "/html/body/div/div[4]/form[2]/table/tbody/tr[" + str(j) + "]/td[3]").text
                self.contact_cache.append(Contact(lastname=lastname, firstname=firstname, id=ids))
                j += 1
                x += 1
        return list(self.contact_cache)
