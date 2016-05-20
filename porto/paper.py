__author__ = 'Fulvio Corno'


class Paper:
    #def __init__(self, eprintid, title, date, type, publication, issn,  ):
    def __init__(self, eprintid, title, date, type):
        # type: (int, str, int, tuple) -> Paper
        self.eprintid = eprintid
        self.title = title
        self.date = date
        self.type = type
        self.authors = []

        self.is_wos = False
        self.impact_wos = 0
        self.is_scopus = False
        self.impact_scopus = 0

    def make_wos(self, impact):
        self.is_wos = True
        self.impact_wos = impact

    def make_scopus(self, impact):
        self.is_scopus = True
        self.impact_scopus = impact
