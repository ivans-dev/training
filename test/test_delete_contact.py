from model.contact import Contact
from random import randrange
from faker import Faker
import pytest

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
        ]


@pytest.mark.parametrize("contact", data, ids=[repr(x) for x in data])
def test_delete_contact(app,contact):
    if app.contact.count() == 0:
        app.contact.add(Contact(contact))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
