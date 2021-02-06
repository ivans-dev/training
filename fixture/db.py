import mysql.connector
from model.group import Group
from model.contact import Contact


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        coursor = self.connection.cursor()
        try:
            coursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in coursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            coursor.close()
        return list

    def get_contact_list(self):
        list = []
        coursor = self.connection.cursor()
        try:
            coursor.execute("select id, address, firstname, lastname, middlename, title, nickname, company, mobile, "
                            "home, "
                            "phone2, work, email, email2, email3 from addressbook")
            for row in coursor:
                (id, address, firstname, lastname, middlename, title, nickname, company, mobile, home, phone2, work,
                 email, email2, email3) = row
                list.append(
                    Contact(id=str(id), address=address, firstname=firstname, lastname=lastname, middlename=middlename,
                            title=title,
                            nickname=nickname, company=company, mobilephone=mobile, homephone=home,
                            secondaryphone=phone2, workphone=work,
                            email=email, email2=email2, email3=email3))
        finally:
            coursor.close()
        return list

    def destroy(self):
        self.connection.close()
