from model.group import  Group
import random


def test_delete_group(app, db, data_groups, check_ui):
    if len(db.get_groups_list()) == 0:
        group = data_groups
        app.group.create(group)
    old_groups = db.get_groups_list()
    group = random.choice(old_groups)
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_groups_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)