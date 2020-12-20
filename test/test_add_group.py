# -*- coding: utf-8 -*-
import pytest

from selenium.common.exceptions import NoAlertPresentException
from model.group import Group
from fixture.application import Application


def is_alert_present(self):
    try:
        self.wd.switch_to_alert()
    except NoAlertPresentException:
        return False
    return True


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name=u"Тестовая", header=u"Тестовая Header", footer=u"Тестовая  Footer"))
    app.session.logout()


def test_add_empty_group(app):
    app.session.login(username="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.session.logout()

# def test_contact(self):
#      wd = self.wd
#     TestContact.open_main_page(wd)
#     TestContact.login(wd, login="admin", password="secret")
#     TestContact.create_contact(wd)
#     TestContact.add_address(wd, Address(u"Российская Федерация, Тульская обалсть, г. Тула"))
#     TestContact.add_contact_info(wd, Contact(firstname="Иванов", lastname="Иван", middlename="Иванович",
#                                                  title="Менеджер"))
#     TestContact.get_main(wd)
#     TestContact.logout(wd)
