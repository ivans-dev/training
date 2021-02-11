from model.contact import Contact
from model.group import Group
import random


def test_del_contact_in_group(app, db, data_groups,data_contacts ,check_ui):
    if len(db.get_groups_list()) == 0:
        group = data_groups
        app.group.create(group)
    if len(db.get_contacts_list()) == 0:
        contact = data_contacts
        app.contact.add(contact)
    if len(db.get_groups_with_contacts()) == 0:
        gs = db.get_group_list()
        g = random.choice(gs)
        cs = db.get_contacts_not_in_group()
        c = random.choice(cs)
        app.contact.add_contact_in_group(c.id, g.id)
    gs = db.get_groups_with_contacts()
    g = random.choice(gs)
    old_contacts = db.get_contacts_in_group()
    c = random.choice(old_contacts)
    app.contact.del_contact_in_group(c.id, g.id)
    new_contacts = db.get_contacts_in_group()
    assert len(old_contacts) - 1 == len(new_contacts)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)