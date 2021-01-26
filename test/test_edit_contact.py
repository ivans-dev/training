from model.contact import Contact
import pytest
import random
from faker import Faker

fake = Faker('ru_RU')
data = [Contact(address=fake.address(), firstname=fake.unique.first_name_male(),
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


@pytest.mark.parametrize("contact", data, ids=[repr(x) for x in data])
def test_edit_contact(app, contact):
    if app.contact.count() == 0:
        app.contact.add(contact)
    old_contacts = app.contact.get_contacts_list()
    index = random.randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
