from model.contact import Contact


def test_delete_contact(app):
    if app.contact.count() == 0:
        app.contact.add(Contact(address="Российская Федерация, Тульская обалсть, г. Тула"))

    app.contact.delete_first()
