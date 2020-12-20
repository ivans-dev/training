from fixture.manager import Manager


def test_add_contact(app):
    Manager.add_contact(app)
