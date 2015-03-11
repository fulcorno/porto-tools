__author__ = 'Fulvio Corno'

"""
Leggi ed analizza il JSON di Porto

NOTA: ecco la URL per ottenere il JSON aggiornato del DAUIN:

http://porto.polito.it/cgi/search/archive/advanced/export_pub_JSON.js?screen=Search&dataset=archive&_action_export=1&output=JSON&exp=0|1|-date%2Fcreators_name%2Ftitle|archive|-|dipartimenti%3Auserdep%3AANY%3AEQ%3AUSER_D1010|-|eprint_status%3Aeprint_status%3AANY%3AEQ%3Aarchive|metadata_visibility%3Ametadata_visibility%3AANY%3AEQ%3Ashow&n=&cache=2663731

"""

import json

dauin = json.load(open('export_pub.json', 'r'))


print len(dauin)

authors = {}

papers = {}

authorship = []

for pub in dauin:
    eprintid = pub['eprintid']
    #print pub.get('date', 0), pub['eprintid'], pub['title']

    # initialize paper entry
    papers[eprintid] = {
        'title': pub['title'],
        'year': pub.get('date', 9999),
        'type': pub['type'],
        'types': pub['types'],
        'authors': []}

    # browse through authors
    for auth in pub['creators']:
        authid = auth['id']

        #print auth['id'], auth['name']['family'], auth['name']['given'], ' ',

        #add to general author dictionary
        if authid not in authors.keys():
            authors[authid] = {'name': auth['name']['family']+' '+auth['name']['given'], 'papers': []}

        # add author -> paper relationship
        authors[authid]['papers'].append(pub['eprintid'])

        # add paper -> author relationship
        papers[eprintid]['authors'].append(authid)
    print


#print authors

#for au in sorted(authors) :
#    print au, authors[au]

productivity = [(authors[au]['name'],  len(authors[au]['papers'])) for au in sorted(authors) if len(authors[au]['papers'])>10]
productivity.sort(key= lambda au: -au[1])
print productivity

types = {(pub['type'], pub['types']) for pub in papers.values()}
print sorted(types)