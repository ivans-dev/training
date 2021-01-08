from model.contact import Contact


def test_edit_contact(app):

    if app.contact.count() == 0:
        app.contact.add(Contact(address="Российская Федерация, Тульская обалсть, г. Тула"))
    old_contacts = app.contact.get_contacts_list()
    app.contact.edit_first(
        Contact(address="Российская Федерация, Тульская обалсть, г. Тула", firstname="Иванов 1", lastname="Иван 1",
                middlename="Иванович 1", title="root", nickname="god", company="Сеть", mobile="79100000000",
                mail="test123@mail.mil"))
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)