from model.group import Group
from faker import Faker
fake = Faker('ru_RU')

constant = [
    Group(name="name1", header="header1", footer="footer1"),
    Group(name="name2", header="header2", footer="footer2")
]

d = fake.words()
data = [Group(name="", header="", footer="")] + [
    Group(name=str(d[1]), header=str(d[1]), footer=str(d[1]))
    for i in range(10)]
