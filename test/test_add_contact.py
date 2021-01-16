from model.contact import Contact


def test_add_contact(app):
    old_contacts = app.contact.get_contacts_list()
    contact = Contact(address="Российская Федерация, Тульская обалсть, г. Тула", firstname="Иванов", lastname="Иван",
                      middlename="Иванович", title="Менеджер", nickname="root", company="Сеть", mobilephone="791234567801",
                      homephone="12345678901", secondaryphone="98765432101", workphone="1234578901",
                      email="test@mail.mil", email2="test2@mail.mil", email3="test3@mail.mil")
    app.contact.add(contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) + 1 == len(new_contacts)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
