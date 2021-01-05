from model.group import Group


def test_add_group(app):
    app.group.create(Group(name=u"Тестовая", header=u"Тестовая Header", footer=u"Тестовая  Footer"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))
