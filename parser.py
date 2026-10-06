from bs4 import BeautifulSoup
from bs4 import MarkupResemblesLocatorWarning 
import requests
import warnings
import questionary
import menu
warnings.filterwarnings("ignore", category=MarkupResemblesLocatorWarning)

def read_html():
    url = input('Saisisez votre URL : ')

    if not url.startswith(("http://", "https://")):
        url = 'https://'+url


    print("Chargement de la requête "+ url +"...\n")


    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        print("Analyse du contenu de la page....\n\n ")
        soupHtml = BeautifulSoup(response.text,'html.parser')
        title = soupHtml.title.string

        description = soupHtml.find('meta',attrs={'name':'description'})

        print("Titre:\n" + title +"\n")

        if description:
            print("Description:\n"+ description['content']+"\n\n")
        else:
            print("Pas de description trouvée.")

        choiceMenu = questionary.select(
            "Que souhaitez-vous faire?",
            choices=["Parser une nouvelle URL", "Quitter"],
            ).ask()

        if(choiceMenu=="Parser une nouvelle URL"):
            read_html()
        else:
            menu.initMenu()

    except requests.exceptions.RequestException:
        print("Impossible d'accéder à cette URL.")

    