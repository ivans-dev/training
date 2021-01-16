from model.contact import Contact
from random import randrange

def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(address="Российская Федерация, Тульская обалсть, г. Тула", firstname="Иванов", lastname="Иван",
                      middlename="Иванович", title="Менеджер", nickname="root", company="Сеть", mobilephone="791234567801",
                      homephone="12345678901", secondaryphone="98765432101", workphone="1234578901",
                      email="test@mail.mil", email2="test2@mail.mil", email3="test3@mail.mil"))
    old_contacts = app.contact.get_contacts_list()
    index = randrange(len(old_contacts))
    app.contact.delete_contact_by_index(index)
    new_contacts = app.contact.get_contacts_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[index:index+1] = []
    assert old_contacts == new_contacts
