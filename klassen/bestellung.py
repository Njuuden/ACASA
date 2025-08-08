from klassen.gerichte import Gerichte

class Bestellung:

    def __init__(self, gerichte:Gerichte) -> None:
        self.bestellung = []
        self.auflistung = ""
        self.kosten = 0
        self.gerichte = gerichte


    def bestellung_aufgeben(self):
        while True:
            eingabe = int(input("\nBitte geben Sie Bestellung auf: > "))
            if eingabe == 0:
                break
            if eingabe not in self.gerichte.verfuegbare_plu:
                print("Leider nicht im Angebot")
                continue
            self.bestellung.append(eingabe)
        self.bestellung.sort()


    def terminalausgabe(self):
        print("\n\nIhre Bestellung lautet wie folgt:")
        print("~"*33) 
        
        for gericht in self.bestellung:
            for kategorie in self.gerichte.karte:
                for auswahl in self.gerichte.karte[kategorie]:
                    if gericht == auswahl['plu']:
                        print(f"{auswahl['plu']}. {auswahl['gericht']} {' ' * (self.gerichte.laenge_gericht - len(auswahl['gericht']))} {auswahl['preis']} €")
                        self.auflistung += f"{auswahl['plu']}. {auswahl['gericht']} {' ' * (self.gerichte.laenge_gericht - len(auswahl['gericht']))} {auswahl['preis']} €\n"
                        self.kosten += auswahl['preis']
        print("\nIhre Bestellung kostet", self.kosten,"€\n")
        print("\nVielen Dank für Ihren Besuch!\n")
        print()