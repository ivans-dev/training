from random import randrange


def test_address_on_home_page(app):
    contacts = app.contact.get_contacts_list()
    index = randrange(len(contacts))
    contact_from_home_page = app.contact.get_contacts_list()[index]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page.address == contact_from_edit_page.address
