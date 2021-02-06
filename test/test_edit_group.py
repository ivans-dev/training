from model.group import Group
import random


def test_edit_group(app, db, data_groups, check_ui):
    group = data_groups
    if len(db.get_group_list()) == 0:
        app.group.create(group)
    old_groups = db.get_group_list()
    random_group = random.choice(old_groups)
    ids = int(random_group.id)
    app.group.modify_group_by_id(ids, group)
    new_groups = db.get_group_list()
    index = old_groups.index(random_group)
    group.id = old_groups[index].id
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)