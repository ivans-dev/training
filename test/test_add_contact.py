from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contacts_list()
    app.contact.add(
        Contact(address="Российская Федерация, Тульская обалсть, г. Тула", firstname="Иванов", lastname="Иван",
                middlename="Иванович", title="Менеджер", nickname="root", company="Сеть",mobile="79123456789",
                mail="test@mail.mil"))

    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts)+1 == len(new_contacts)