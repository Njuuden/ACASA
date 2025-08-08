from klassen.kunde import Kunde
from klassen.bestellung import Bestellung

class Quittung:

    def __init__(self, kunde:Kunde, bestellung:Bestellung ) -> None:
        self.kunde = kunde
        self.bestellung = bestellung


    def quittung_erzeugen(self):

        with open(f"./Quittungen/{self.kunde.nachname}.txt", mode= "a", encoding= "UTF-8") as datei:
            datei.write(f"\nQuittung für {self.kunde.vorname} {self.kunde.nachname} \n")
            datei.write("~" * (14 + len(self.kunde.vorname) + len(self.kunde.nachname)))
            datei.write("\n")
            datei.write(self.bestellung.auflistung)
            datei.write(f"\nIhre Bestellung kostet {self.bestellung.kosten} €\n")
            datei.write("\nVielen Dank für Ihren Besuch!\n\n")