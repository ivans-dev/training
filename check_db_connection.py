from fixture.orm import ORMFixture

db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

print(db.get_info_contact("phone", 202)[0])