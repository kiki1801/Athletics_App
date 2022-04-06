# Track and Field Results Browser and Winner Probability Model ![25%](https://progress-bar.dev/25)

- [About the Project](#about-the-project)
- [Build With](#build-with)
- [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
  * [Usage](#usage)
- [Contributor](#contributor)

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

Now, you can run the `main.py` file and follow the instructions on your Python console.
Below, you can see a demo. 

First, I chose to launch the browser in English. Then I wanted to keep the competitions of the last 2 weeks.

![Screen 1](https://user-images.githubusercontent.com/98753607/161865916-4ed93373-003c-4ff6-88e0-f056e990aa63.png)

Now, you need to choose the feature you want to use.

   - First one : **__"Look at the top N Marks"__**

Here, I picked the first one by typing 1 in the console. But I didn't want to restrict to a specific nationality (If you pick yes, you have to choose the one you want to select from a list). Then, I chose **N = 15**, so I will only see the 15 best marks later. Finally, I wanted to check out the men's pole vault results. That's why I selected consecutively : **Men**, **Jumps** and **Pole Vault**.
Now, you get what you were looking for.

![Screen 2](https://user-images.githubusercontent.com/98753607/161865921-09514d92-0de2-4da5-82f1-582ee6c88406.png)

I also made examples for others features : 

   - Second one : **__"Any Records ?"__**

![Screen 3](https://user-images.githubusercontent.com/98753607/161865927-008aa532-4e5f-414a-ad17-ad20f44995ec.png)

   - Third one : **__"Winning Probability ?"__**

![Screen 4](https://user-images.githubusercontent.com/98753607/161865937-e91a998d-8786-475c-83e2-3a7b2c19f729.png)

# Contributor

- **Kyllian James** ([@kyllianj](https://github.com/kyllianj))
- [LinkedIn](https://www.linkedin.com/in/kyllianjames/) 
