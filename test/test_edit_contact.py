from model.contact import Contact


def test_edit_contact(app):
    contact = Contact(address="Российская Федерация, Тульская обалсть, г. Тула", firstname="Иванов 1",
                      lastname="Иван 1",
                      middlename="Иванович 1", title="root", nickname="god", company="Сеть", mobile="79100000000",
                      mail="test123@mail.mil")
    if app.contact.count() == 0:
        app.contact.add(contact)
    old_contacts = app.contact.get_contacts_list()
    contact.id = old_contacts[0].id
    app.contact.edit_first(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
