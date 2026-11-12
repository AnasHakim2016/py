from daten import lade_mitglieder
from darstellung import formatiere_bericht

def main():
    mitglieder = lade_mitglieder()
    print(formatiere_bericht(mitglieder))

if __name__ == "__main__":
    main()