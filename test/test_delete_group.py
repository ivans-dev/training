from model.group import Group
from random import randrange
from faker import Faker
import pytest

fake = Faker('ru_RU')

data = [Group(name="", header="", footer="")] + [
    Group(name=fake.unique.bs(), header=fake.unique.bs(), footer=fake.unique.bs())
     ]


@pytest.mark.parametrize("group", data, ids=[repr(x) for x in data])
def test_delete_group(app, group):
    if app.group.count() == 0:
        app.group.create(group)
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    app.group.delete_group_by_index(index)
    new_groups = app.group.get_group_list()
    assert len(old_groups) - 1 == len(new_groups)
    old_groups[index:index + 1] = []
    assert old_groups == new_groups
