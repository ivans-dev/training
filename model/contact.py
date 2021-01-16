from sys import maxsize


class Contact:
    def __init__(self, address=None, firstname=None, lastname=None, middlename=None, title=None, nickname=None,
                 company=None, mobilephone=None, workphone=None, secondaryphone=None, homephone=None, id=None,
                 all_phones_from_home_page=None,
                 email=None, email2=None, email3=None, all_emails_from_home_page=None):
        self.firstname = firstname
        self.lastname = lastname
        self.title = title
        self.middlename = middlename
        self.address = address
        self.nickname = nickname
        self.company = company
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.homephone = homephone
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s %s %s %s " % (self.id, self.firstname, self.all_phones_from_home_page, self.all_emails_from_home_page)

    def __eq__(self, other):
        return (
                       self.id is None or other.id is None or self.id == other.id) and \
               self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
