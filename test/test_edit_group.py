from model.group import Group


def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))
    old_groups = app.group.get_group_list()
    app.group.edit_first(Group(name="Тестовая 1"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)

