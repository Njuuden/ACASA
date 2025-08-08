import json

class Gerichte:

    def __init__(self) -> None:
        self.karte = {}
        self.verfuegbare_plu = []
        self.laenge_gericht = 0


    def menu_einlesen(self):

        with open("./Karte/menu.json", mode = "r", encoding= "UTF-8") as datei:
            self.karte = json.load(datei)
        return self.karte


    def karte_anzeigen(self):
        
        for kategorie in self.karte:
            for auswahl in self.karte[kategorie]:
                if len(auswahl['gericht']) > self.laenge_gericht:
                    self.laenge_gericht = len(auswahl['gericht'])
        
        for kategorie in self.karte:
            print("\n", kategorie, "\n", "~"*len(kategorie))
            for auswahl in self.karte[kategorie]:
                print(f"{auswahl['plu']}. {auswahl['gericht']} {' ' * (self.laenge_gericht - len(auswahl['gericht']))} {auswahl['preis']} €")
                self.verfuegbare_plu.append(auswahl['plu'])