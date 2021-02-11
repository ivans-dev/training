from model.contact import Contact
from model.group import Group
import random


def test_add_contact_in_group(app, db, data_groups,data_contacts, check_ui):
    if len(db.get_groups_list()) == 0:
        group = data_groups
        app.group.create(group)
    if len(db.get_contacts_list()) == 0:
        contact = data_contacts
        app.contact.add(contact)
    old_contacts = db.get_contacts_not_in_group()
    c = random.choice(old_contacts)
    gs = db.get_group_list()
    g = random.choice(gs)
    app.contact.add_contact_in_group(c.id, g.id)
    new_contacts = db.get_contacts_not_in_group()
    assert len(old_contacts) - 1 == len(new_contacts)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                         key=Contact.id_or_max)