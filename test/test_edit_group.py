from model.group import Group

def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(name=u"Тестовая 1", header=u"Тестовая Header 2", footer=u"Тестовая  Footer 3"))
    app.session.logout()