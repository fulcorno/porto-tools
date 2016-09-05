from porto.author import Author
import requests
import codecs

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
]

baseURL = "http://porto.polito.it/cgi/exportview/creators/"
output_basedir = "./cached_js/"

def scarica_autore(author):
    name = author.lastname + '=3A' + author.firstname + '=3A' + author.id + '=3A'+'.js'

    portoURL = baseURL+name+"/JSON/"+name
    filename = output_basedir+name

    r = requests.get(portoURL)

    try:
        porto_json = r.json()
        print "%s has %d papers" % (author.lastname, len(porto_json))

        porto_text = r.text

        f = codecs.open(filename, "w", encoding="utf-8")
        f.write(porto_text)
        f.close()
    except ValueError:
        print "ERROR in processing %s", author.lastname

if __name__=="__main__":

    for author in authors:
        scarica_autore(author)
