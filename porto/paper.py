__author__ = 'Fulvio Corno'


class Paper:
    #def __init__(self, eprintid, title, date, type, publication, issn,  ):
    def __init__(self, eprintid, title, date, type, abstract="", uri=""):
        # type: (int, str, int, tuple) -> Paper
        self.eprintid = eprintid
        self.title = title
        self.date = date
        self.type = type

        self.abstract = abstract

        self.authors = []

        self.is_wos = False
        self.impact_wos = 0
        self.is_scopus = False
        self.impact_scopus = 0

        self.issn = None
        self.isbn = None
        self.publisher = None
        self.event_title = None
        self.book_title = None
        self.publication = None
        self.DOI = None # called id_number in JSON
        self.uri = None
        self.pages = None


    def make_wos(self, impact):
        self.is_wos = True
        self.impact_wos = impact

    def make_scopus(self, impact):
        self.is_scopus = True
        self.impact_scopus = impact
