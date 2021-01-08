from sys import maxsize


class Contact:
    def __init__(self, address=None, firstname=None, lastname=None, middlename=None, title=None, nickname=None,
                 company=None, mobile=None, mail=None, id=None):
        self.firstname = firstname
        self.lastname = lastname
        self.title = title
        self.middlename = middlename
        self.address = address
        self.nickname = nickname
        self.company = company
        self.mobile = mobile
        self.mail = mail
        self.id = id

    def __repr__(self):
        return "%s:%s" % (self.id, self.firstname)

    def __eq__(self, other):
        return (
                           self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(ct):
        if ct.id:
            return int(ct.id)
        else:
            return maxsize
