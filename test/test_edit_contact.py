from model.contact import Contact
from random import randrange


def test_edit_contact(app):
    contact = Contact(address="Российская Федерация, Тульская обалсть, г. Тула", firstname="Иванов", lastname="Иван",
                      middlename="Иванович", title="Менеджер", nickname="root", company="Сеть", mobilephone="791234567801",
                      homephone="12345678901", secondaryphone="98765432101", workphone="1234578901",
                      email="test@mail.mil", email2="test2@mail.mil", email3="test3@mail.mil")
    if app.contact.count() == 0:
        app.contact.add(contact)
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    contact.id = old_contacts[index].id
    app.contact.modify_contact_by_index(index, contact)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
