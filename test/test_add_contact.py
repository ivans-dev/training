import pytest

from selenium.common.exceptions import NoAlertPresentException
from model.contact import Contact
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


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.add(Contact(address="Российская Федерация, Тульская обалсть, г. Тула", firstname="Иванов", lastname="Иван", middlename="Иванович", title="Менеджер"))
    app.session.logout()