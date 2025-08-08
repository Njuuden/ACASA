import os 
from pathlib import Path 
os.chdir(Path(__file__).parent)

from klassen.gerichte import Gerichte
from klassen.kunde import Kunde
from klassen.bestellung import Bestellung
from klassen.quittung import Quittung

print("\nACASA Projekt\n")

def main():
    
    kunde = Kunde()
    kunde.namensabfrage()
    kunde.willkommenstext()
    
    gerichte = Gerichte()
    gerichte.menu_einlesen()
    gerichte.karte_anzeigen()

    bestellung = Bestellung(gerichte)
    bestellung.bestellung_aufgeben()
    bestellung.terminalausgabe()

    quittung = Quittung(kunde, bestellung)
    quittung.quittung_erzeugen()

if __name__ == "__main__":
    main()