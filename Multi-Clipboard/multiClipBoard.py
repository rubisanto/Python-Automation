from distutils.cmd import Command
import sys
import clipboard
import json


SAVED_DATA = "clipborad.json"

# créer un json


def save_data(filepath, data):
    with open(filepath, 'w') as f:
        json.dump(data, f)

# lire le json


def load_data(filepath):
    # si le fichier n'existe pas, on le crée
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
        return data
    except:
        return {}


# utiliser dépuis la commande ou terminal
# verifier si seulement une commande
if len(sys.argv) == 2:
    command = sys.argv[1]
    data = load_data(SAVED_DATA)

    if command == "save":
        key = input("Entrez la clé: ")
        # sauvegarder
        data[key] = clipboard.paste()
        save_data(SAVED_DATA, data)
        print("Données sauvegardées")
    elif command == "load":
        key = input("Entrez la clé:")
        if key in data:

            clipboard.copy(data[key])
            print("Données copiées")
        else:
            print("La clé n'existe pas")
    elif command == "list":
        print(data)
else:
    print("Please pass exactly one argument")
