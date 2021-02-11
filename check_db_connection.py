from fixture.orm import ORMFixture
from model.group import Group
db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

print (db.get_contacts_in_group("255"))
