import re


def test_address_on_home_page(app, db):
    contacts = app.contact.get_contacts_list()
    for contact in contacts:
        contact_from_home_page = contact
        adr2 = db.get_info_contact("address", contact.id)[0]
        adr1 = contact_from_home_page.address
        assert adr1 == adr2


def test_emails_on_home_page(app, db):
    contacts = app.contact.get_contacts_list()
    for contact in contacts:
        contact_from_home_page = contact
        assert contact_from_home_page.all_emails_from_home_page == merge_emails_like_on_home_page(
            list(db.get_info_contact("mail", contact.id)[0]))


def test_name_on_home_page(app, db):
    contacts = app.contact.get_contacts_list()
    for contact in contacts:
        contact_from_home_page = contact
        assert contact_from_home_page.firstname == db.get_info_contact("firstname", contact.id)[0]
        assert contact_from_home_page.lastname == db.get_info_contact("lastname", contact.id)[0]


def test_phones_on_home_page(app, db):
    contacts = app.contact.get_contacts_list()
    for contact in contacts:
        contact_from_home_page = contact
        assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(
            list(db.get_info_contact("phone", contact.id)[0]))




def clear(s):
    return re.sub("[() -]", "", s)


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       contact))))


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       contact))))
