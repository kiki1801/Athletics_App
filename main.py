#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 11:31:02 2022

@author: Kyllian James
"""

#0 - Library
import pandas as pd
from bs4 import BeautifulSoup
import re
import urllib3
import json 
import datetime
import pycountry

#0 - Import function form other file
from function_all import choice,create_calendar_links,get_competitions_infos,filter_competitions_df,create_results_links,get_iso_code

#Welcome Message
print('Welcome to the IAAF browser competitions results and probability model of future winners !')
print('')

#1 - Choose your language
language_list = ['English','French']

choice(language_list)
language = int(input('Choose your language : '))

#PROGRAM IN ENGLISH OR IN FRENCH
if language == 1:
    #1A - Create links for IAAF calendar pages
    calendar_urls = create_calendar_links()
    
    #1B - Get information of each competition on each calendar's page
    competition_infos_df = get_competitions_infos(calendar_urls)
    
    #1C - Keep only competitions we need
    number_of_weeks = int(input('How many past weeks you want to keep ? : '))
    filtered_df = filter_competitions_df(competition_infos_df,number_of_weeks)
    
    #1D - Create links for competitions results pages
    results_urls = create_results_links(filtered_df)
    
    #2 - Choose between 3 features
    features_list = ['Look at the Top N Marks','Any Records ?','Winning Probability ?']
    choice(features_list)
    feature = int(input('Select one feature : '))
    
    #2A - Look at the Top N Marks
    if feature == 1:
        #Tell yes if you want to check for a specific nationality
        yes_no_list = ['Yes','No']
        choice(yes_no_list)
        yes_no = int(input('Do you want to look at the top N marks for a specific nationality ? '))
        
        if yes_no == 1:
            #Choose a nationality and then run the same code as if you don't want to look for a specific nationality
            list_iso_code = get_iso_code()
            choice(list_iso_code)
            iso_code = input('Choose one by typing his ISO code : ')
            print('')
            print('Coming Soon...')
        else:
            number_of_marks = int(input('Top N Marks ? Choose N : '))
            
            #Choose between Men and Women
            genders_list = ['Men','Women']
            choice(genders_list) 
            gender = int(input('Select one : '))
            
            if gender == 1:
                #Choose between type of event
                event_types_list = ['Races','Jumps','Throws']
                choice(event_types_list)
                event_type = int(input('Which kind of events ? '))
                
                if event_type == 1:
                    #Choose a race event
                    races_list = ["60m","100m","200m","400m","60mH","110mH","400mH","800m","1500m","3000m","3000mSC","5000m","10000m"]
                    choice(races_list)
                    race = int(input('Select one : '))
                    print('Coming Soon...')
                elif event_type == 2:
                    #Choose a jump event
                    jumps_list = ["Long Jump","Triple Jump","High Jump","Pole Vault"]
                    choice(jumps_list)
                    race = int(input('Select one : '))
                    print('Coming Soon...')
                else:
                    #Choose a throw event
                    throws_list = ["Shot Put","Discus Throw","Hammer Throw","Javelin Throw"]
                    choice(throws_list)
                    race = int(input('Select one : '))
                    print('Coming Soon...')
            else:
                #Choose between type of event
                event_types_list = ['Races','Jumps','Throws']
                choice(event_types_list)
                event_type = int(input('Which kind of events ? '))
                
                if event_type == 1:
                    #Choose a race event
                    races_list = ["60m","100m","200m","400m","60mH","100mH","400mH","800m","1500m","3000m","3000mSC","5000m","10000m"]
                    choice(races_list)
                    race = int(input('Select one : '))
                    print('Coming Soon...')
                elif event_type == 2:
                    #Choose a jump event
                    jumps_list = ["Long Jump","Triple Jump","High Jump","Pole Vault"]
                    choice(jumps_list)
                    race = int(input('Select one : '))
                    print('Coming Soon...')
                else:
                    #Choose a throw event
                    throws_list = ["Shot Put","Discus Throw","Hammer Throw","Javelin Throw"]
                    choice(throws_list)
                    race = int(input('Select one : '))
                    print('Coming Soon...')
    #2B - Any Records ?
    elif feature == 2:
        print('Coming Soon...')
    #2C - Winning Probability ?
    else:
        #Choose between Men and Women
        genders_list = ['Men','Women']
        choice(genders_list) 
        gender = int(input('Select one : '))
        
        if gender == 1:
            #Choose between type of event
            event_types_list = ['Races','Jumps','Throws']
            choice(event_types_list)
            event_type = int(input('Which kind of events ? '))
            
            if event_type == 1:
                #Choose a race event
                races_list = ["60m","100m","200m","400m","60mH","110mH","400mH","800m","1500m","3000m","3000mSC","5000m","10000m"]
                choice(races_list)
                race = int(input('Select one : '))
                print('Coming Soon...')
            elif event_type == 2:
                #Choose a jump event
                jumps_list = ["Long Jump","Triple Jump","High Jump","Pole Vault"]
                choice(jumps_list)
                race = int(input('Select one : '))
                print('Coming Soon...')
            else:
                #Choose a throw event
                throws_list = ["Shot Put","Discus Throw","Hammer Throw","Javelin Throw"]
                choice(throws_list)
                race = int(input('Select one : '))
                print('Coming Soon...')
        else:
            #Choose between type of event
            event_types_list = ['Races','Jumps','Throws']
            choice(event_types_list)
            event_type = int(input('Which kind of events ? '))
            
            if event_type == 1:
                #Choose a race event
                races_list = ["60m","100m","200m","400m","60mH","100mH","400mH","800m","1500m","3000m","3000mSC","5000m","10000m"]
                choice(races_list)
                race = int(input('Select one : '))
                print('Coming Soon...')
            elif event_type == 2:
                #Choose a jump event
                jumps_list = ["Long Jump","Triple Jump","High Jump","Pole Vault"]
                choice(jumps_list)
                race = int(input('Select one : '))
                print('Coming Soon...')
            else:
                #Choose a throw event
                throws_list = ["Shot Put","Discus Throw","Hammer Throw","Javelin Throw"]
                choice(throws_list)
                race = int(input('Select one : '))
                print('Coming Soon...')
else:
    #1A - Créer les liens des pages du calendrier IAAF
    calendar_urls = create_calendar_links()
    
    #1B - Scrap les informations de chaque compétition de chaque page du calendrier
    competition_infos_df = get_competitions_infos(calendar_urls)
    
    #1C - Filtrer le tableau des compétitions
    number_of_weeks = int(input('Combien de semaines passées vous voulez garder ? : '))
    filtered_df = filter_df(competition_infos_df,number_of_weeks)
    
    #1D - Créer les liens des pages de résultats de chaque compétition
    results_urls = create_results_links()
    
    #2 - Choisir entre 3 fonctionnalités 
    features_list = ['Regardez les N meilleures performances','Nouveaux Records ?',"Probabilité de l'emporter ?"]
    choice(features_list)
    feature = int(input('Sélectionner une fonctionnalité : '))
    
    #2A - Regardez les N meilleures performances
    if feature == 1:
        yes_no_list = ['Oui','Non']
        choice(yes_no_list)
        yes_no = int(input('Voulez-vous consulter les N meilleures performances pour une nationalité spécifique ?'))
        
        if yes_no == 1:
            list_iso_code = get_iso_code()
            choice(list_iso_code)
            iso_code = input('Choisissez-en un en écrivant son code ISO : ')
            print('')
            print('Prochainement...')
        else:
            number_of_marks = int(input('N Meilleures Performances ? Choisissez N : '))
            
            genders_list = ['Homme','Femme']
            choice(genders_list) 
            gender = int(input('Sélectionnez-en un : '))
            
            if gender == 1:
                event_types_list = ['Courses','Sauts','Lancers']
                choice(event_types_list)
                event_type = int(input('Quel type de disciplines ? '))
                
                if event_type == 1:
                    races_list = ["60m","100m","200m","400m","60mH","110mH","400mH","800m","1500m","3000m","3000mSC","5000m","10000m"]
                    choice(races_list)
                    race = int(input('Sélectionnez-en un : '))
                    print('Prochainement...')
                elif event_type == 2:
                    jumps_list = ["Saut en Longueur","Triple Saut","Saut en Hauteur","Saut à la Perche"]
                    choice(jumps_list)
                    race = int(input('Sélectionnez-en un : '))
                    print('Prochainement...')
                else:
                    throws_list = ["Lancer de Poids","Lancer de Disque","Lancer de Marteau","Lancer de Javelot"]
                    choice(throws_list)
                    race = int(input('Sélectionnez-en un : '))
                    print('Prochainement...')
            else:
                event_types_list = ['Courses','Sauts','Lancers']
                choice(event_types_list)
                event_type = int(input('Quel type de disciplines ? '))
                
                if event_type == 1:
                    races_list = ["60m","100m","200m","400m","60mH","100mH","400mH","800m","1500m","3000m","3000mSC","5000m","10000m"]
                    choice(races_list)
                    race = int(input('Sélectionnez-en un : '))
                    print('Prochainement...')
                elif event_type == 2:
                    jumps_list = ["Saut en Longueur","Triple Saut","Saut en Hauteur","Saut à la Perche"]
                    choice(jumps_list)
                    race = int(input('Sélectionnez-en un : '))
                    print('Prochainement...')
                else:
                    throws_list = ["Lancer de Poids","Lancer de Disque","Lancer de Marteau","Lancer de Javelot"]
                    choice(throws_list)
                    race = int(input('Sélectionnez-en un : '))
                    print('Prochainement...')
    #2B - Nouveaux Records ?
    elif feature == 2:
        print('Prochainement...')
    #2C - Probabilité de l'emporter ?
    else:
        genders_list = ['Homme','Femme']
        choice(genders_list) 
        gender = int(input('Sélectionnez-en un : '))
        
        if gender == 1:
            event_types_list = ['Courses','Sauts','Lancers']
            choice(event_types_list)
            event_type = int(input('Quel type de disciplines ? '))
            
            if event_type == 1:
                races_list = ["60m","100m","200m","400m","60mH","110mH","400mH","800m","1500m","3000m","3000mSC","5000m","10000m"]
                choice(races_list)
                race = int(input('Sélectionnez-en un : '))
                print('Prochainement...')
            elif event_type == 2:
                jumps_list = ["Saut en Longueur","Triple Saut","Saut en Hauteur","Saut à la Perche"]
                choice(jumps_list)
                race = int(input('Sélectionnez-en un : '))
                print('Prochainement...')
            else:
                throws_list = ["Lancer de Poids","Lancer de Disque","Lancer de Marteau","Lancer de Javelot"]
                choice(throws_list)
                race = int(input('Sélectionnez-en un : '))
                print('Prochainement...')
        else:
            event_types_list = ['Courses','Sauts','Lancers']
            choice(event_types_list)
            event_type = int(input('Quel type de disciplines ? '))
            
            if event_type == 1:
                races_list = ["60m","100m","200m","400m","60mH","100mH","400mH","800m","1500m","3000m","3000mSC","5000m","10000m"]
                choice(races_list)
                race = int(input('Sélectionnez-en un : '))
                print('Prochainement...')
            elif event_type == 2:
                jumps_list = ["Saut en Longueur","Triple Saut","Saut en Hauteur","Saut à la Perche"]
                choice(jumps_list)
                race = int(input('Sélectionnez-en un : '))
                print('Prochainement...')
            else:
                throws_list = ["Lancer de Poids","Lancer de Disque","Lancer de Marteau","Lancer de Javelot"]
                choice(throws_list)
                race = int(input('Sélectionnez-en un : '))
                print('Prochainement...')
