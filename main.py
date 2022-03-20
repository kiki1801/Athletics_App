#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 11:31:02 2022

@author: kyllian
"""

#0 - Library
import pandas as pd
from bs4 import BeautifulSoup
import re
import urllib3
import json 
import datetime

#0 - Import function form other file
from function_all import choice,create_calendar_links,get_competitions_infos,filter_df

#1 - Choose your language
language_list = ['English','French']

choice(language_list)
language = int(input('Choose your language : '))

#PROGRAM IN ENGLISH OR IN FRENCH
if language == 1:
    print('Coming Soon...')
    #A - Create links for IAAF calendar pages
    calendar_urls = create_calendar_links()
    
    #B - Get information of each competition on each calendar's page
    competition_infos_df = get_competitions_infos(calendar_urls)
    
    #C - Keep only competitions we need
    number_of_weeks = int(input('How many past weeks you want to keep ? : '))
else:
    print('Prochainement...')
    #A - Créer les liens pour les pages du calendrier IAAF
    calendar_urls = create_calendar_links()
    
    #B - Scrap les informations de chaque compétition de chaque page du calendrier
    competition_infos_df = get_competitions_infos(calendar_urls)
    
    #C - Filtrer le tableau des compétitions
    number_of_weeks = int(input('Combien de semaines passées vous voulez garder ? : '))
    filtered_df = filter_df(competition_infos_df,number_of_weeks)





