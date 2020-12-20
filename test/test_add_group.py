from fixture.manager import Manager


def test_group(app):
    Manager.add_group(app)


def test_empty_group(app):
    Manager.add_empty_group(app)
