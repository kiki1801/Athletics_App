# Track and Field Results Browser and Winner Probability Model ![25%](https://progress-bar.dev/25)


# Table of Contents

- [About the Project](#about-the-project)
- [Build With](#build-with)
- [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
  * [Usage](#usage)
- [Contributor](#contributor)

# About the Project

This browser is based on a web scraping project made during my first year of master's degree ([kiki1801/M1_Web_Scraping_IAAF](https://github.com/kiki1801/M1_Web_Scraping_IAAF)).

It consists of doing web scraping on the calendar of competitions of the International Association of Athletics Federations ([IAAF](https://worldathletics.org/competition/calendar-results?)) in order to obtain all the results of the last n weeks. 

![IAAF](https://user-images.githubusercontent.com/98753607/162062744-de7b4c2d-6ab4-436c-a9a0-5385b860831d.png)

From these results I created three different features, to look at the top k performances for each discipline, to check if any records have been broken recently and there is also a probability model to predict who will have the most chance to win in future competitions.

This project can be useful to stay informed about the latest best results in athletics. Thanks to the first feature, it gives us an idea of who dominates his/her discipline currently. The odds of winning help us know who is most likely to win based on recent past results.

Features I hope to implement in the near future : 
 - [ ] Coding to choose a specific nationality in the first feature **__"Look at the top N Marks"__**.
 - [ ] Add the next competition start list in the probability model to only compute odds for athletes who will perform.
 - [ ] Add relays, combined events and race walking in the browser.
 - [ ] Add wind for outdoor events.
 - [ ] Create a graphics window to see the output in a nicer way.

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

- **Kyllian James** ([@kiki1801](https://github.com/kiki1801))
- [LinkedIn](https://www.linkedin.com/in/kyllianjames/) 
