from model.contact import Contact
from faker import Faker
import os
import jsonpickle
import argparse

n = 5
f = 'data/contacts.json'
parse = argparse.ArgumentParser(description='Генерация файла с данными для группы')
parse.add_argument('-n', type=int, default=n, help='Количество генерируемы данных')
parse.add_argument('-f', type=str, default=f, help='Имя файла')

my_args = parse.parse_args()
f = my_args.f
n = my_args.n

fake = Faker('ru_RU')
testdata = [Contact(address=fake.unique.address(), firstname=fake.unique.first_name_male(),
                    lastname=fake.unique.last_name_male(),
                    middlename=fake.unique.first_name_male(), title=fake.unique.job(),
                    nickname=fake.unique.first_name_male(), company=fake.unique.company(),
                    mobilephone=fake.unique.phone_number(),
                    homephone=fake.unique.phone_number(), secondaryphone=fake.unique.phone_number(),
                    workphone=fake.unique.phone_number(),
                    email=fake.unique.ascii_free_email(), email2=fake.unique.ascii_free_email(),
                    email3=fake.unique.ascii_free_email())
            for i in range(n)
            ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)
with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))
