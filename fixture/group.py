class GroupHelper:
    def __init__(self, app):
        self.app = app

    def open_groups_pages(self):
        wd = self.app.wd
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_pages()
        wd.find_element_by_name("new").click()
        self.group_element(group)
        wd.find_element_by_name("submit").click()
        self.return_to_groups_page()

    def delete_first_group(self):
        wd = self.select_first_group()
        wd.find_element_by_xpath("(//input[@name='delete'])[2]").click()
        self.return_to_groups_page()

    def edit_first(self, group):
        wd = self.select_first_group()
        wd.find_element_by_xpath("(//input[@name='edit'])[2]").click()
        self.group_element(group)
        wd.find_element_by_name("update").click()
        wd.find_element_by_link_text("group page").click()

    def select_first_group(self):
        wd = self.app.wd
        self.open_groups_pages()
        wd.find_element_by_name("selected[]").click()
        return wd

    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()

    def group_element(self, group):
        self.change_field_value("group_name", group.name)
        self.change_field_value("group_header", group.header)
        self.change_field_value("group_footer", group.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def count(self):
        wd = self.app.wd
        self.open_groups_pages()
        return len(wd.find_elements_by_name("selected[]"))