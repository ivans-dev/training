from model.contact import Contact
from faker import Faker
import os
import json
import getopt
import sys


fake = Faker('ru_RU')
data = [Contact(address=fake.unique.address(), firstname=fake.unique.first_name_male(),
                lastname=fake.unique.last_name_male(),
                middlename=fake.unique.first_name_male(), title=fake.unique.job(),
                nickname=fake.unique.first_name_male(), company=fake.unique.company(),
                mobilephone=fake.unique.phone_number(),
                homephone=fake.unique.phone_number(), secondaryphone=fake.unique.phone_number(),
                workphone=fake.unique.phone_number(),
                email=fake.unique.ascii_free_email(), email2=fake.unique.ascii_free_email(),
                email3=fake.unique.ascii_free_email())
        for i in range(10)
        ]
file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "../data/contacts.json")
with open(file, "w")  as f:
    f.write(json.dumps(data, default=lambda x: x.__dict__, indent=2))