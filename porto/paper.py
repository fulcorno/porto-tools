__author__ = 'Fulvio Corno'


class Paper:

    def __init__(self, eprintid, title, date, type):
        self.eprintid = eprintid
        self.title = title
        self.date = date
        self.type = type
        self.authors = []

