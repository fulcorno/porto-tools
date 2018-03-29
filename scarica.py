# coding: utf-8
from porto import Author
import requests
import codecs
import begin
import json

baseURL = "http://porto.polito.it/cgi/exportview/creators/"
default_output_directory = "./cached_js"
default_authors_file = "./authors.json"


def load_authors(authors_file):
    json_authors = json.load(open(authors_file))
    authors = []
    for jauth in json_authors:
        authors.append(Author(id=jauth['id'], lastname=jauth['last'], firstname=jauth['first']))
    return authors


def download_author(author, output_dir):

    name = author.lastname + '=3A' + author.firstname + '=3A' + author.id + '=3A' + '.js'

    portoURL = baseURL + name + "/JSON/" + name
    r = requests.get(portoURL)

    try:
        porto_json = r.json()
        print("%s has %d papers" % (author, len(porto_json)))

        #porto_text = r.text

        filename = output_dir + "/" + name

        try:
            f = codecs.open(filename, "w", encoding="utf-8")
        except IOError:
            print("ERROR in creating %s" % filename)
            return

        f.write(r.text)
        f.close()
    except ValueError:
        print("ERROR in processing %s", author.lastname)


@begin.start(auto_convert=True)
def run(list=False, all=False, authors_file=default_authors_file, output_directory=default_output_directory,  *selected):
    """
    Scarica automaticamente pubblicazioni dal PORTO in formato JSON.

    Opzioni:
        scarica --list
            stampa l'elenco degli autori noti al programma

        scarica (default)
            scarica e salva le pubblicazioni di TUTTI gli autori noti

        scarica <id> <id> <id> ...
            scarica e salva solo le pubblicazioni degli autori citati
            <id> può essere una matricola autore
            <id> può essere una parte (substring, case-insensitive) del cognome autore
            in caso di match multipli, vale solo il primo
    """

    authors = load_authors(authors_file)

    # filter selection
    if all:
        if len(selected)>0:
            print("ERROR: --all and selection list are incompatible options")
            exit()
    else:
        if len(selected)>0:
            authors = [a for a in authors if
                       a.matricola() in [("000000"+s)[-6:] for s in selected]
                       or a.lastname.lower() in [s.lower() for s in selected]]
        else:
            print("WARNING: no author selected. Nothing to do. Use --all or provide list of IDs or surnames")
            exit()

    if list:
        print("Selected authors:")
        for author in authors:
            print("{author.id}: {author.lastname} {author.firstname}".format(author=author))
    else:
        print("Downloading selected authors in %s" % output_directory)
        for author in authors:
            print("Downloading author: %s" % author)
            download_author(author, output_directory)
