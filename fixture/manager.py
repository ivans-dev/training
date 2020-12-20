from model.contact import Contact
from model.group import Group


class Manager:
    def __init__(self, app):

        self.app = app

    def add_group(self):
        self.app.session.login(username="admin", password="secret")
        self.app.group.create(Group(name=u"Тестовая", header=u"Тестовая Header", footer=u"Тестовая  Footer"))
        self.app.session.logout()

    def add_empty_group(self):
        self.app.session.login(username="admin", password="secret")
        self.app.group.create(Group(name="", header="", footer=""))
        self.app.session.logout()

    def add_contact(self):
        self.session.login(username="admin", password="secret")
        self.contact.add(
            Contact(address="Российская Федерация, Тульская обалсть, г. Тула", firstname="Иванов", lastname="Иван",
                    middlename="Иванович", title="Менеджер"))
        self.session.logout()
