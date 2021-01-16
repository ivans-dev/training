from sys import maxsize


class Contact:
    def __init__(self, address=None, firstname=None, lastname=None, middlename=None, title=None, nickname=None,
                 company=None, mobilephone=None, workphone=None, secondaryphone=None, mail=None, id=None):
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
        self.mail = mail
        self.id = id

    def __repr__(self):
        return "%s:%s %s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (
                           self.id is None or other.id is None or self.id == other.id) and \
               self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
