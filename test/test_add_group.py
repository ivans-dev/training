from model.group import Group
import pytest
from faker import Faker
fake = Faker('ru_RU')

data = [Group(name="", header="", footer="")] + [
    Group(name=fake.unique.words(), header=fake.unique.words(), footer=fake.unique.words())
    for i in range(10)]


@pytest.mark.parametrize("group", data, ids=[repr(x) for x in data])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
