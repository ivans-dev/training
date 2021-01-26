from model.group import Group
import pytest
import random
from faker import Faker

fake = Faker('ru_RU')

data = [Group(name="", header="", footer="")] + [
    Group(name=fake.unique.words(), header=fake.unique.words(), footer=fake.unique.words())
    for i in range(10)
]


@pytest.mark.parametrize("group", data, ids=[repr(x) for x in data])
def test_edit_group(app, group):
    if app.group.count() == 0:
        app.group.create(group)
    old_groups = app.group.get_group_list()
    index = random.randrange(len(old_groups))
    group.id = old_groups[index].id
    app.group.modify_group_by_index(index, group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
