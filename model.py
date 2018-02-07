from porto.type import Type
from porto.author import Author
from porto.paper import Paper
import portoDAO

class Model:

    def __init__(self):
        self.allPapers = {}
        self.allAuthors = {}
        # self.allTypes = set()

    def fromJSON(self, jsondoc):
        for pub in jsondoc:
            eprintid = pub['eprintid']

            thisType = Type(pub['type'], pub['types'])

            thisPaper = Paper(eprintid, pub['title'], pub.get('date', 9999), thisType, abstract=pub.get('abstract', ""))

            # populate ancillary fields

            if ('wos' in pub):
                thisPaper.make_wos(pub['wos']['impact'])

            if ('scopus' in pub):
                thisPaper.make_scopus(pub['scopus']['impact'])

            thisPaper.issn = pub.get('issn', None)
            thisPaper.isbn = pub.get('isbn', None)
            thisPaper.publisher = pub.get('publisher', None)
            thisPaper.event_title = pub.get('event_title', None)
            thisPaper.book_title = pub.get('book_title', None)
            thisPaper.publication = pub.get('publication', None)
            thisPaper.DOI = pub.get('id_number', None)
            thisPaper.uri = pub.get('uri', None)
            thisPaper.pages = pub.get('pages', None)

            # store paper
            self.allPapers[eprintid] = thisPaper

            # browse through authors
            for auth in pub['creators']:
                authid = auth['id']

                thisAuthor = Author(authid, auth['name']['family'], auth['name']['given'])

                if thisAuthor not in self.allAuthors:
                    self.allAuthors[authid] = thisAuthor

                thisPaper.authors.append(self.allAuthors[authid])

        print("Loaded %d papers" % len(self.allPapers))
        print("Found %d authors" % len(self.allAuthors))

    def saveSQL(self):

        DAO = portoDAO.DAO()

        # dump all papers
        #DAO.delete_all_papers()

        for id in self.allPapers:
            DAO.create_paper(self.allPapers[id])

        # dump all authors
        for au in self.allAuthors:
            DAO.create_author(self.allAuthors[au])

        # dump paper<>author relationship
        for id in self.allPapers:
            for au in self.allPapers[id].authors:
                # print "paper %d author %d" % (id, au.id)
                DAO.create_paper_author(self.allPapers[id], au)

        DAO.close()