__author__ = 'Fulvio Corno'

"""
Leggi ed analizza il JSON di Porto
"""

import json

dauin = json.load(open('export_pub.json', 'r'))

print len(dauin)

authors = {}

papers = {}

authorship = []

for pub in dauin:
    print pub.get('date', 0), pub['eprintid'], pub['title']
    papers[pub['eprintid']] = {'title': pub['title'], 'year': pub.get('date', 9999), 'authors': []}
    for auth in pub['creators']:
        print auth['id'], auth['name']['family'], auth['name']['given'], ' ',
        if auth['id'] not in authors.keys():
            authors[auth['id']] = {'name': auth['name']['family']+' '+auth['name']['given'], 'papers': []}
        authors[auth['id']]['papers'].append(pub['eprintid'])
        papers[pub['eprintid']]['authors'].append(auth['id'])
    print


#print authors

for au in sorted(authors) :
    print au, authors[au]

productivity = [ (authors[au]['name'],  len(authors[au]['papers'])) for au in sorted(authors)]
productivity.sort(key= lambda au: -au[1])
print productivity