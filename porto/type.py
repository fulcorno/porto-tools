__author__ = 'Fulvio Corno'

class Type:

    def __init__(self, type, types):
        self.type = type
        self.types = types

"""
article TYPES2 - Articolo in rivista
article TYPES70 - Recensione in rivista -- una sola: "eprintid": 1398199, "date": 2005,
article TYPES73 - Abstract in rivista
book TYPES6 - Monografia o trattato scientifico
book TYPES87 - Traduzione di libro -- esiste uno solo (potrebbe essere Traduzione di Libro):  "eprintid": 2501611, "date": 2000,
book_section TYPES4 - Contributo in volume( Capitolo o Saggio)
book_section TYPES76 - Prefazione/Postfazione
book_section TYPES77 - Breve introduzione
book_section TYPES78 - Voce di dizionario/enciclopedia
conference_item TYPES8 - Contributo in atti di convegno
conference_item TYPES89 - Abstract in atti di convegno
conference_item TYPES90 - Poster
editorship TYPES12 - Curatela
other TYPES103 - Software
other TYPES14 - Altro
patent TYPES10 - Brevetto
thesis TYPES110 - Tesi di dottorato - Altri enti
thesis TYPES16 - Tesi di dottorato - Polito
"""