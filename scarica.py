# coding: utf-8
from porto.author import Author
import requests
import codecs
import begin

authors = [
    Author(firstname="Fulvio", lastname="Corno", id="002154"),
    Author(firstname="Dario", lastname="Bonino", id="012325"),
    Author(firstname="Luigi", lastname="De Russis", id="025734"),
    Author(firstname="Sebastian", lastname="Aced Lopez", id="027070"),
    Author(firstname="Faisal", lastname="Razzak", id="023127"),
    Author(firstname="Muhammad", lastname="Sanaullah", id="024462"),
    Author(firstname="Laura", lastname="Farinetti", id="002236"),
    Author(firstname="Teodoro", lastname="Montanaro", id="036541"),
    Author(firstname="Alberto", lastname="Monge Roffarello", id="040637"),
    Author(firstname="Juan Pablo", lastname="Saenz", id="042870"),
]

baseURL = "http://porto.polito.it/cgi/exportview/creators/"
default_output_dir = "./cached_js"


def scarica_autore(author, output_dir):

    name = author.lastname + '=3A' + author.firstname + '=3A' + author.id + '=3A' + '.js'

    portoURL = baseURL + name + "/JSON/" + name
    r = requests.get(portoURL)

    try:
        porto_json = r.json()
        print "%s has %d papers" % (author, len(porto_json))

        #porto_text = r.text

        filename = output_dir + "/" + name

        try:
            f = codecs.open(filename, "w", encoding="utf-8")
        except IOError:
            print "ERROR in creating %s" % filename
            return

        f.write(r.text)
        f.close()
    except ValueError:
        print "ERROR in processing %s", author.lastname


@begin.start(auto_convert=True)
def run(list=False, directory=default_output_dir, *selected):
    """
    Scarica automaticamente pubblicazioni dal PORTO in formato JSON.

    Opzioni:
        scarica --list
            stampa l'elenco degli autori noti al programma

        scarica (default)
            scarica e salva le pubblicazioni di TUTTI gli autori noti

        scarica <id> <id> <id> ...
            scarica e salva solo le pubblicazioni degli autori citati
            <id> può essere una parte (substring) della matricola autore
            <id> può essere una parte (substring, case-insensitive) del cognome autore
            in caso di match multipli, vale solo il primo
    """

    if list == True:
        print "Known authors:"
        for author in authors:
            print "%s: %s %s" % (author.id, author.lastname, author.firstname)
    elif len(selected) == 0:
        # print all
        print "Downloading all authors in %s" % directory
        for author in authors:
            print "Downloading author: %s" % author
            scarica_autore(author, directory)
    else:
        print "Downloading authors matching: %s" % str(selected)
        for sel in selected:
            sel_author = [a for a in authors if (sel in a.id or sel.lower() in a.lastname.lower())]
            if(len(sel_author)==1):
                #print sel_author[0]
                scarica_autore(sel_author[0], directory)
