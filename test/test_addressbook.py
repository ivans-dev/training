from fixture.manager import Manager
from fixture.application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_group(app):
    Manager.add_group(app)


def test_empty_group(app):
    Manager.add_empty_group(app)


def test_contact(app):
    Manager.add_contact(app)
