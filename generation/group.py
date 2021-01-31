from model.group import Group
from faker import Faker
import os
import jsonpickle
import argparse

n = 5
f = 'data/groups.json'
parse = argparse.ArgumentParser(description='Генерация файла с данными для контактов')
parse.add_argument('-n', type=int, default=n, help='Количество генерируемы данных')
parse.add_argument('-f', type=str, default=f, help='Имя файла')

my_args = parse.parse_args()
f = my_args.f
n = my_args.n
fake = Faker('ru_RU')
testdata = [Group(name="", header="", footer="")] + [
    Group(name=fake.unique.name(), header=fake.unique.job(), footer=fake.unique.bs())
    for i in range(n)]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
