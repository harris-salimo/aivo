# AIVO
AIVO signifie **_"Analyse d'Image et Vision par Ordinateur"_** est un projet (application de traitement d'image) scolaire réalisé par groupe.

## Langage utilisée
AIVO est dévelloppé avec le langage **Python**.

## Auteurs
Comme ce projet est un travail de groupe vous pouvez trouvez les noms de tous les contributeurs dans [ce fichier](CONTRIBUTORS.txt).

## Installation
### Python
  Pour ce projet, on a utilisé la [version 3](runtime.txt) de python. Pour verifier quelle version de python vous avez, tapez le commande ci-dessous dans votre invite de commande selon votre système d'exploitation. Ou alors téléchargez en cliquant sur [ce lien](https://python.org/downloads).
  - Si vous êtes sous Window: 
`python --version`
  - Si vous êtes sous Linux ou sous OS X:
`python3 --version`

### Pré-requis
Le programme necessite certains pré-requis cités dans [ce fichier](requirements.txt) pour mieux fonctionner. Pour les installer, tapez simplement ces commandes en bas dans votre invite de commande selon votre cas.
- Si vous utilisez Windows:
  `pip install -r requirements.txt`
- Si vous utilisez Linux ou OS X:
  `pip3 install -r requirements.txt`

## Execution
Dans le dossier `src` vous trouverez deux fichier `.py` (`main.py` et `tools.py`) qui sont tous les deux indispensable pour le bon fonctionnement du programme:
- `main.py`: contient toutes les configurations sur l'interface du programme.
- `tools.py`: contient toutes les implémentations des algorithmes de traitement d'image étudiés en cours.

Pour executer le programme, tapez seulement la commande ci-dessous dans votre invite de commande selon votre système d'exploitation.
- Sous Windows:
  `python src/main.py`
- Sous Linux ou OS X:
  `python3 src/main.py`

#### NB (_Pour Linux seulement_): Ce programme utilise la librarie `tkinter` pour l'interface graphique et la module `ImageTk` du librairie `Pillow` pour charger une image dans l'interface graphique. Ce dernier peut produire une erreur si elle n'est pas installée alors verifiez l'installation en executant 
`>>> import tkinter`\
`>>> from PIL import ImageTk`
### Puis `Enter` dans l'interpreteur de python.
Pour ouvrir l'interpreteur tapez juste `python` si vous êtes sous Windows ou `python3` si vous êtes sous Linux/OS X dans votre invite de commande.

## Test
Et vous pouvez tester avec [cette image](images/Lena.png) contenu dans le dossier images.
