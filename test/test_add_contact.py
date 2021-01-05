from model.contact import Contact


def test_add_contact(app):
    app.contact.add(
        Contact(address="Российская Федерация, Тульская обалсть, г. Тула", firstname="Иванов", lastname="Иван",
                middlename="Иванович", title="Менеджер", nickname="root", company="Сеть",mobile="79123456789",
                mail="test@mail.mil"))
