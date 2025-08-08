class Kunde:

    def __init__(self) -> None:
        self.nachname = ""
        self.vorname = ""

      
    def namensabfrage(self):
        self.nachname = input("Bitte geben Sie Ihren Nachnamen ein: ").strip().upper()
        self.vorname = input("Bitte geben Sie Ihren Vornamen ein: ").strip().title()
    

    def willkommenstext(self):
        print("\n\n    Willkommen im ACASA-Restaurant Herr/Frau", self.nachname)
        print("~"*(49+len(self.nachname)))
        print("\nBitte wählen Sie aus dem folgenden Menü aus:")
        print("(Mit der '0' beenden Sie Ihre Bestellung.)\n")