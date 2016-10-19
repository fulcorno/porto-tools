__author__ = 'Fulvio Corno'

class Author:

    def __init__(self, id, lastname, firstname):
        self.id = id
        self.lastname = lastname
        self.firstname = firstname

    def name(self):
        return self.lastname.upper()+" "+self.firstname

    def matricola(self):
        return ("000000"+str(self.id))[-6:]

    def __repr__(self):
        return self.name()
