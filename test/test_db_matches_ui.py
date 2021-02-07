from model.group import Group
from model.contact import Contact


def test_group_liset(app, db):
    ui_list = app.group.get_group_list()

    def clean(group):
        return Group(id=group.id, name=group.name.strip())

    db_list = map(clean, db.get_groups_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


def test_contact_list(app, db):
    ui_list = app.contact.get_contacts_list()

    def clean(contact):
        return Contact(id=contact.id, address=contact.address.strip(), firstname=contact.firstname.strip(),
                       lastname=contact.lastname.strip(), middlename=contact.middlename.strip(),
                       title=contact.title.strip(), nickname=contact.nickname.strip(), company=contact.company.strip(),
                       mobilephone=contact.mobilephone.strip(), homephone=contact.homephone.strip(),
                       secondaryphone=contact.secondaryphone.strip(), workphone=contact.workphone.strip(),
                       email=contact.email.strip(), email2=contact.email2.strip(), email3=contact.email3.strip())

    db_list = map(clean, db.get_contacts_list())
    assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)
