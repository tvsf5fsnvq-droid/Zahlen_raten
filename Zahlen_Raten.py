^import random


def zahlenratespiel():
    """Die Hauptfunktion für das Zahlenratespiel."""

    print("Willkommen beim Zahlenratespiel! 🔢")
    print("Ich denke mir eine Zahl zwischen 1 und 100 aus...")

    # 1. Zufallszahl generieren
    geheimzahl = random.randint(1, 100)
    versuche = 0

    while True:
        try:
            # 2. Versuchszähler erhöhen
            versuche += 1

            # 3. Benutzereingabe
            geratene_zahl_str = input("Gib deinen Tipp ein: ")
            geratene_zahl = int(geratene_zahl_str)

            # 4. Feedback-Logik
            if geratene_zahl < geheimzahl:
                print("Zu niedrig! Versuche es mit einer höheren Zahl.")
            elif geratene_zahl > geheimzahl:
                print("Zu hoch! Versuche es mit einer kleineren Zahl.")
            else:
                # 5. Erfolg und Spielende
                print(f"\n🎉 Glückwunsch! Du hast die Zahl {geheimzahl} erraten!")
                print(f"Du hast nur {versuche} Versuche benötigt.")
                break  # Die Schleife verlassen und das Spiel beenden

        except ValueError:
            # Fehler abfangen, falls der Benutzer Text statt einer Zahl eingibt
            print("Das war keine gültige Zahl. Bitte gib eine ganze Zahl ein.")
            continue  # Springe zur nächsten Runde der Schleife


if __name__ == '__main__':
    zahlenratespiel()