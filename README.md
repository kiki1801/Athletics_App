# Track and Field Results Browser and Winner Probability Model (In Progress)

# About the Project

Soon...

<!-- This navigator is based on a web scraping project in my first year's master degree ([kyllianj/M1_Web_Scraping_IAAF](https://github.com/kyllianj/M1_Web_Scraping_IAAF))

Il consiste à faire du web scraping sur le calendrier des compétitions du site de l'Association Internationale des Fédérations d'Athlétisme ([IAAF](https://worldathletics.org/competition/calendar-results?) en anglais) afin de d'envoyer un mail récapitulatif des meilleures performances d'athlétisme, relativement à des seuils fixés, réalisées au cours des quatre dernières semaines écoulées. 

Ce récapitulatif des performances est pratique pour se tenir informer des résultats récents notamment dans le cas où on a pas le temps de regarder toutes les compétitions, ni accès aux plateformes de diffusion, et aussi dans le cas où la compétition n'est pas diffusé.\
Il peut aussi servir à avoir une idée des athlètes qui dominent une discipline et des athlètes en forme dernièrement sur chaque discipline.\
Ainsi, cela donne une brève intuition de quel athlète est favori sur chaque discipline pour les compétitions à venir.\
En quelque sorte, ce projet pourrait permettre de prédire les futurs vainqueurs des prochaines compétitions. 

![Capture d’écran 2022-04-01 à 11 31 11](https://user-images.githubusercontent.com/98753607/161236875-4302259d-3984-48aa-ad13-efbb8cbbcb2f.png)

Some of the challenges you faced and features you hope to implement in the future.

3. Table of Contents (Optional) -->


# Build With 

- [Anaconda Navigator](https://www.anaconda.com/products/distribution)
- **Spyder** 5.1.5
- **Python** 3.9.7

# Getting Started

## Prerequisites

To begin with, make sure you have installed all the packages necessary to run the code properly.

In your terminal use the following command in order to install all the packages used for this project according to the configuration file `requirements.txt` :
   ```sh
   pip install -r requirements.txt
   ```
   
## Installation

You must copy raw contents of the `main.py` and `function_all.py` files.
Make sure you have these two files in the same working directory. If not, you need to modify the code in line 19 in the `main.py` file by adding the name of the folder where `function_all.py` is saved : 
   ```sh
   from folder.function_all import
   ```
Soon more explanations...

## Usage

Now, you can run the `main.py` file.

Just below you can see a demo where I chose to lauch the browser in English.
Then I kept 2 weeks of interest in the results of the competitions.
choix englais puis deux semaines

![Screen 1](https://user-images.githubusercontent.com/98753607/161865916-4ed93373-003c-4ff6-88e0-f056e990aa63.png)

choix premiere fonctionnalité -> loot at top N mark 
no specific nationality, if u choose yes -> then u have to choose which nationality between a list of ones
Choix 15 top mark
choix homem 
choix look for jumps
pole vault

![Screen 2](https://user-images.githubusercontent.com/98753607/161865921-09514d92-0de2-4da5-82f1-582ee6c88406.png)

Maintenant si suite choix nombre semaine j'avais choisi l'option 2 -> any record, voici resultat

![Screen 3](https://user-images.githubusercontent.com/98753607/161865927-008aa532-4e5f-414a-ad17-ad20f44995ec.png)

Si fonctionnalité 3, comme fonctionnalité 1 -> choix femme ici puis choix course puis le 100m 

![Screen 4](https://user-images.githubusercontent.com/98753607/161865937-e91a998d-8786-475c-83e2-3a7b2c19f729.png)


Soon more explanations...

# Contributor

- **Kyllian James** ([@kyllianj](https://github.com/kyllianj))
- [LinkedIn](https://www.linkedin.com/in/kyllianjames/) 
