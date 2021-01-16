from model.group import Group
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits  + string.punctuation+" " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


data = [Group(name="", header="", footer="")] + [
    Group(name=random_string("name", 15), header=random_string("header", 23), footer=random_string("footer", 30))
    for i in range(10)]


@pytest.mark.parametrize("group", data, ids=[repr(x) for x in data])
def test_add_group(app, group):
    old_groups = app.group.get_group_list()
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
