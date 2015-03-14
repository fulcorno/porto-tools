__author__ = 'Fulvio Corno'

"""
Leggi ed analizza il JSON di Porto

NOTA: ecco la URL per ottenere il JSON aggiornato del DAUIN:

http://porto.polito.it/cgi/search/archive/advanced/export_pub_JSON.js?screen=Search&dataset=archive&_action_export=1&output=JSON&exp=0|1|-date%2Fcreators_name%2Ftitle|archive|-|dipartimenti%3Auserdep%3AANY%3AEQ%3AUSER_D1010|-|eprint_status%3Aeprint_status%3AANY%3AEQ%3Aarchive|metadata_visibility%3Ametadata_visibility%3AANY%3AEQ%3Ashow&n=&cache=2663731

"""

import json

from porto.paper2 import Paper
from porto.type2 import Type
from porto.author import Author

dauin = json.load(open('export_pub.json', 'r'))

allPapers = {}
allTypes = set()
allAuthors = {}

for pub in dauin:
    eprintid = pub['eprintid']

    #TODO: CHECK allTypes
    thisType = Type(pub['type'], pub['types'])
    if thisType not in allTypes:   #DOESN'T WORK: CREATES DUPLICATES
        allTypes.add(thisType)

    thisPaper = Paper(eprintid, pub['title'], pub.get('date', 9999), thisType)

    allPapers[eprintid] = thisPaper

    # browse through authors
    for auth in pub['creators']:
        authid = auth['id']

        thisAuthor = Author(authid, auth['name']['family'], auth['name']['given'])

        if thisAuthor not in allAuthors:
            allAuthors[authid] = thisAuthor

        thisPaper.authors.append(thisAuthor)

print "Loaded %d papers" % len(allPapers)
print "Found %d authors" % len(allAuthors)
print "Found %d types" % len(allTypes)
#print allAuthors.values()
