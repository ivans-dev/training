from random import randrange


def test_name_on_home_page(app):
    contacts = app.contact.get_contacts_list()
    index = randrange(len(contacts))
    contact_from_home_page = app.contact.get_contacts_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.firstname == contact_from_edit_page.firstname
    assert contact_from_home_page.lastname == contact_from_edit_page.lastname
    assert contact_from_home_page.middlename == contact_from_edit_page.middlename
    assert contact_from_home_page.nickname == contact_from_edit_page.nickname
