__author__ = 'Fulvio Corno'

"""
Leggi ed analizza il JSON di Porto

NOTA: ecco la URL per ottenere il JSON aggiornato del DAUIN:

http://porto.polito.it/cgi/search/archive/advanced/export_pub_JSON.js?screen=Search&dataset=archive&_action_export=1&output=JSON&exp=0|1|-date%2Fcreators_name%2Ftitle|archive|-|dipartimenti%3Auserdep%3AANY%3AEQ%3AUSER_D1010|-|eprint_status%3Aeprint_status%3AANY%3AEQ%3Aarchive|metadata_visibility%3Ametadata_visibility%3AANY%3AEQ%3Ashow&n=&cache=2663731

"""

import json, gzip

from porto.paper import Paper
from porto.author import Author

dauin = json.load(gzip.open('export_pub.json.gz', 'r'))

#dauin = json.load(open('export_pub.json', 'r'))

allPapers = {}
allTypes = set()
allAuthors = {}

for pub in dauin:
    eprintid = pub['eprintid']

    thisType = (pub['type'], pub['types'])
    if thisType not in allTypes:
        allTypes.add(thisType)

    thisPaper = Paper(eprintid, pub['title'], pub.get('date', 9999), thisType)

    if('wos' in pub):
        thisPaper.make_wos(pub['wos']['impact'])

    if('scopus' in pub):
        thisPaper.make_scopus(pub['scopus']['impact'])


    allPapers[eprintid] = thisPaper

    # browse through authors
    for auth in pub['creators']:
        authid = auth['id']

        thisAuthor = Author(authid, auth['name']['family'], auth['name']['given'])

        if thisAuthor not in allAuthors:
            allAuthors[authid] = thisAuthor

        thisPaper.authors.append(allAuthors[authid])

print "Loaded %d papers" % len(allPapers)
print "Found %d authors" % len(allAuthors)
print "Found %d types (from %d main types)" % (len(allTypes), len({a for (a,b) in allTypes}))
print sorted(allTypes)
for t in sorted(allTypes):
    print t[0]+"/"+t[1], len( [paper for paper in allPapers if (allPapers[paper].type[1] == t[1])] )#

print "ALL PAPERS"
for y in range(1995,2017):
    print y, len( [paper for paper in allPapers if (allPapers[paper].date == y)] )

print "JOURNAL PAPERS (TYPES2)"
for y in range(1995,2017):
    print y, len( [paper for paper in allPapers if (allPapers[paper].date == y and allPapers[paper].type[1]=="TYPES2")] )
