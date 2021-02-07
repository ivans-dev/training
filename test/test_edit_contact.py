from model.contact import Contact
import random


def test_edit_contact(app, db, data_contacts, check_ui):
    contact = data_contacts
    if app.contact.count() == 0:
        app.contact.add(contact)
    old_contacts = db.get_contacts_list()
    random_contact = random.choice(old_contacts)
    ids = int(random_contact.id)

    app.contact.modify_contact_by_id(ids, contact)
    new_contacts = db.get_contacts_list()
    index = old_contacts.index(random_contact)
    contact.id = old_contacts[index].id
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contacts_list(), key=Contact.id_or_max)
