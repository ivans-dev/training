from model.group import Group


def test_edit_group(app):
    app.group.edit_first(Group(name=u"Тестовая 1"))
