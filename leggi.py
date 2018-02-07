from porto.paper import Paper
from porto.author import Author
from porto.type import Type

__author__ = 'Fulvio Corno'

"""
Leggi ed analizza il JSON di Porto

NOTA: ecco la URL per ottenere il JSON aggiornato del DAUIN:

http://porto.polito.it/cgi/search/archive/advanced/export_pub_JSON.js?screen=Search&dataset=archive&_action_export=1&output=JSON&exp=0|1|-date%2Fcreators_name%2Ftitle|archive|-|dipartimenti%3Auserdep%3AANY%3AEQ%3AUSER_D1010|-|eprint_status%3Aeprint_status%3AANY%3AEQ%3Aarchive|metadata_visibility%3Ametadata_visibility%3AANY%3AEQ%3Ashow&n=&cache=2663731


ALTRE URL... scoperte per tentativi

http://porto.polito.it/cgi/exportview/divisions/DAUIN/2011/JSON/DAUIN.json

http://porto.polito.it/cgi/exportview/divisions/DAUIN/JSON/DAUIN.json

http://porto.polito.it/cgi/exportview/creators/Corno=3AFulvio=3A002154=3A/2016/JSON/Corno=3AFulvio=3A002154=3A.js
"""

import json, gzip


dauin = json.load(gzip.open('DAUIN.json.gz', 'r'))

#dauin = json.load(open('DAUIN.json', 'r'))

allPapers = {}
allTypes = set()
allAuthors = {}

for pub in dauin:
    eprintid = pub['eprintid']

    #thisType = (pub['type'], pub['types'])
    thisType = Type(pub['type'], pub['types'])
    if thisType not in allTypes:
        allTypes.add(thisType)

    thisPaper = Paper(eprintid, pub['title'], pub.get('date', 9999), thisType, abstract=pub.get('abstract', ""))

    if('wos' in pub):
        thisPaper.make_wos(pub['wos']['impact'])

    if('scopus' in pub):
        thisPaper.make_scopus(pub['scopus']['impact'])

    allPapers[eprintid] = thisPaper

    # browse through authors
    for auth in pub['creators']:
        if 'id' in auth:
            authid = auth['id']

            thisAuthor = Author(authid, auth['name']['family'], auth['name']['given'])

            if thisAuthor not in allAuthors:
                allAuthors[authid] = thisAuthor

            thisPaper.authors.append(allAuthors[authid])
        else:
            print("Author %s not found in paper %s" % (
                auth['name']['family'] + " " + auth['name']['given'],
                eprintid))

print("Loaded %d papers" % len(allPapers))
print("Found %d authors" % len(allAuthors))

print("Found %d types (from %d main types)" % (len(allTypes), len({a.type for a in allTypes})))
print(allTypes)
for t in sorted(allTypes):
    print(t, len([paper for paper in allPapers if (allPapers[paper].type.types == t.types)]))

yearRange = range(1995, 2017)

stats = {(year, type): 0 for type in allTypes for year in yearRange}

for eprintid, thisPaper in allPapers.items():
    if thisPaper.date in yearRange:
        stats[(thisPaper.date,thisPaper.type)] += 1

print(0, [t.description for t in allTypes])
for year in yearRange:
    row = [stats[(year, type)] for type in allTypes]
    print(year, row)

"""
print "ALL PAPERS"
for y in range(1995,2017):
    print y, len( [paper for paper in allPapers if (allPapers[paper].date == y)] )

print "JOURNAL PAPERS (TYPES2)"
for y in range(1995,2017):
    print y, len( [paper for paper in allPapers if (allPapers[paper].date == y and allPapers[paper].type.types=="TYPES2")] )
"""