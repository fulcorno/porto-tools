import porto
import begin
from model import Model

__author__ = 'Fulvio Corno'


import json, gzip

@begin.start(auto_convert=True)
def run(*filenames):
    """
    Reads the specified JSON files and insert the corresponding
    papers and authors into the SQL database.
    """

    model = Model()

    try:
        for filename in filenames:
            print "Loading %s" % filename
            doc = json.load(open(filename, 'r'))
            model.fromJSON(doc)
    except IOError as e:
        print "Error in processing %s" % filename
        print e

    print "Saving into database"
    model.saveSQL()

""""
print "Found %d types (from %d main types)" % (len(allTypes), len({a.type for a in allTypes}))
print allTypes
for t in sorted(allTypes):
    print t, len([paper for paper in allPapers if (allPapers[paper].type.types == t.types)])

yearRange = range(1995, 2017)

stats = {(year, type): 0 for type in allTypes for year in yearRange}

for eprintid, thisPaper in allPapers.items():
    if thisPaper.date in yearRange:
        stats[(thisPaper.date,thisPaper.type)] += 1

print 0, [t.description for t in allTypes]
for year in yearRange:
    row = [stats[(year, type)] for type in allTypes]
    print year, row
"""

"""
print "ALL PAPERS"
for y in range(1995,2017):
    print y, len( [paper for paper in allPapers if (allPapers[paper].date == y)] )

print "JOURNAL PAPERS (TYPES2)"
for y in range(1995,2017):
    print y, len( [paper for paper in allPapers if (allPapers[paper].date == y and allPapers[paper].type.types=="TYPES2")] )
"""