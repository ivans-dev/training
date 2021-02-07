import re


def test_address_on_home_page(app,db):
    contacts = app.contact.get_contacts_list()
    for contact in contacts:
        contact_from_home_page = contact
        assert contact_from_home_page.address == db.get_info_contact("address", contact.id)[0]


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


#
# def test_phones_on_contact_view_page(app):
#     contacts = app.contact.get_contacts_list()
#     index = randrange(len(contacts))
#     contact_from_view_page = app.contact.get_contact_from_view_page(index)
#     contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
#     assert contact_from_view_page.homephone == contact_from_edit_page.homephone
#     assert contact_from_view_page.mobilephone == contact_from_edit_page.mobilephone
#     assert contact_from_view_page.secondaryphone == contact_from_edit_page.secondaryphone
#     assert contact_from_view_page.workphone == contact_from_edit_page.workphone


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
