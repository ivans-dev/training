from model.contact import Contact
import pytest
import random
import string


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits  + " " * 2
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_number(maxlen):
    return "".join([random.choice(string.digits) for i in range(random.randrange(maxlen))])


def random_email(emaillen):
    return ''.join(random.choice(string.ascii_letters) for x in range(emaillen))


data = [Contact(address=random_string("address", 20), firstname=random_string("firstname", 8),
                lastname=random_string("lastname", 10),
                middlename=random_string("middlename", 10), title=random_string("titile", 10),
                nickname=random_string("nickname", 5), company=random_string("company", 10),
                mobilephone=random_number(11),
                homephone=random_number(11), secondaryphone=random_number(11), workphone=random_number(11),
                email=random_email(10) + "@mail.ru", email2=random_email(5) + "@mail.ru",
                email3=random_email(16) + "@mail.ru")
        for i in range(5)
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
