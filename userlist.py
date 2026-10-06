import questionary
import menu
import csv

users = [] ;

def edit_users():
    if len(users)  == 0:
        choiceUsers=["Ajouter un utilisateur","Revenir au menu principal"]
    elif len(users) == 1:
        choiceUsers=['Ajouter un utilisateur', "Vider la liste","Revenir au menu principal"]
    elif len(users) > 1:
        choiceUsers=['Ajouter un utilisateur','Supprimer un utilisateur', 'Vider la Liste','Revenir au menu principal',"Exporter dans un fichier CSV"]
    
    choiceUsersSelected = questionary.select("Que voulez-vous faire?",choices=choiceUsers).ask()
    
    if choiceUsersSelected == "Ajouter un utilisateur":
        createUser()
        edit_users()
    elif choiceUsersSelected == "Revenir au menu principal":
        menu.initMenu()
    elif choiceUsersSelected == "Exporter dans un fichier CSV":
        exportToCSV()
    elif choiceUsersSelected == "Vider la Liste":
        users=[]
        print('La liste a été vidée')
        edit_users()

def createUser():
    answers = questionary.form(
        firstname = questionary.text("Enter your firstname: "),
        lastname = questionary.text("Enter your lastname: "),
        email = questionary.text("Enter your email: "),
    ).ask()

    for user in users:
        if user["email"] == answers['email']:
            print('un utilisateur existe deja avec cet email! ')
            return
    users.append(answers)
    print(users)

def exportToCSV():

    en_tete = ['firstname','lastname','email' ]
    with open('output/list.csv', 'w') as fichier_csv:
        writer = csv.writer(fichier_csv, delimiter=',')
        writer.writerow(en_tete)
        for user in users:
            writer.writerow([user["firstname"],user["lastname"],user["email"]])
        print('Le fichier a été généré dans le dossier uploads')
    edit_users()
