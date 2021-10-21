# Installation du scrapper books
## Cloner le repo github en local

Lancer dans le terminal:

***git clone https://github.com/gsysaath/scrapper_python.git scrapper***

Rentrons dans le dossier tout juste cloné:

***cd scrapper***
## Tout d'abord creer l'environnement virtuel

Lancez dans le terminal la commande qui va vous creer l'envrironnement virtuel appelé env:

- Pour Unix:

    ***python3 -m venv env***

- Pour windows:

    ***python -m venv env***
    
Activons le:
- Pour Unix:

    ***source ./env/bin/activate***
- Pour Windows:

    ***.env/Scripts/activate.bat***

## Installer les requirements

    pip install -r requirements.txt

## Et lancer le scrapping:

- Pour Unix:

    ***python3 scrapper.py***

- Pour windows:

    ***python scrapper.py*** 
