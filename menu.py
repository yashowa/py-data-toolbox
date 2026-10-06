

import questionary
import userlist
import parser

def initMenu():
    print("\033[2J\033[H", end="")
    choicesMenu = questionary.select("Que souhaitez-vous faire?",choices=[ "Parser une URL", "Editer une liste d'utilisateurs","Quitter l'application"]).ask()

    print(choicesMenu.upper())
    print("=======================================================>\n")

    match choicesMenu:
        case "Parser une URL":
            parser.read_html()
            return
        case "Editer une liste d'utilisateurs":
            userlist.edit_users()
        case "Quitter l'application":
            exit()
            return
        case _:
            print("Aucun choix")
