#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 11:33:18 2022

@author: Kyllian James
"""

#Function to make choice while running the code
def choice(list_of_choice):
    i = 1
    for element in list_of_choice:
        print('{} : {}'.format(str(i),element))
        i = i+1

###############################################################################
        
#1A - Create links for IAAF calendar pages        
#Create links for IAAF calendar pages
def create_calendar_links():
    calendar_urls = ['https://www.worldathletics.org/competition/calendar-results?']
    for i in range(100,15*100,100):
        things_make_link = ['https://www.worldathletics.org/competition/calendar-results?offset=',str(i)]    
        calendar_url = ''.join(things_make_link)
        calendar_urls.append(calendar_url) 
        
    return calendar_urls

###############################################################################

#1B - Get informations of each competition on each calendar's page
#Library
import pandas as pd
from bs4 import BeautifulSoup
import re
import urllib3
import json 

#Function for scraping 
def get_content(regex,url):
    req = urllib3.PoolManager()
    res = req.request('GET',url)
    soup = BeautifulSoup(res.data,'html.parser')
    content = soup.find_all(regex)
    
    return content
    
def get_competitions_infos(list_with_urls):
    empty_df = pd.DataFrame()
    for link in list_with_urls:
        content = get_content('script',link)
        content = content[1]
        
        json_object = content.text
        get_dict = json.loads(json_object)
        infos_dict = get_dict["props"]["pageProps"]["initialEvents"]['results']
        
        df = pd.DataFrame(infos_dict)
        empty_df = pd.concat([empty_df,df])
        
        empty_df = empty_df.reset_index(drop=True)
    
    return empty_df

###############################################################################

#1C - Keep only competitions we need
#Library 
import datetime

#Keep the ones between today and n past weeks
def filter_df(dataframe,n):
    #Keep the ones with results
    dataframe_bis = dataframe.loc[(dataframe['hasResults'] == True )]
        
    #Delete row with NA in column disciplines -> Race Walking 
    dataframe_bis = dataframe_bis[dataframe_bis['disciplines'].notna()]

    #Keep Stadium Indoor & Outdoor
    dataframe_bis = dataframe_bis[dataframe_bis['disciplines'].str.contains('Stadium Indoor|Stadium Outdoor')]
    
    today = datetime.date.today()
    date_n_weeks_before = today - datetime.timedelta(weeks=n)
    
    dataframe_bis['endDate'] = pd.to_datetime(dataframe_bis['endDate']).dt.date
    filtered_df = dataframe_bis[(dataframe_bis['endDate'] >= date_n_weeks_before)]
    
    filtered_df = filtered_df.reset_index(drop=True)
    
    return filtered_df

###############################################################################

#1D - Create links for competitions results pages
def create_results_links():
    #Links for day 1
    results_urls = []
    for identity in list(filtered_df['id']):
        things_make_results_link = ['https://www.worldathletics.org/competition/calendar-results/results/',str(identity)]
        results_url = ''.join(things_make_results_link)
        results_urls.append(results_url)
           
    #Links for days 2 until n
    #Create new column in filtered_df
    filtered_df['startDate'] = pd.to_datetime(filtered_df['startDate']).dt.date
    filtered_df['Number_of_days'] = filtered_df['endDate'] - filtered_df['startDate'] 

    #Loop on index to keep only competitions with Number_of_days > 0
    index_list = list(filtered_df.index)
    for k in index_list:
        if filtered_df['Number_of_days'][k].days == 0:
            filtered_df_clean = filtered_df.drop(labels=k, axis=0)

    #Reset filtered_df index        
    filtered_df_clean = filtered_df_clean.reset_index(drop=True)

    #Loop again on index       
    for index in list(filtered_df_clean.index):
        n_days = filtered_df_clean['Number_of_days'][index].days + 2
        for j in range(2,n_days):
            things_to_make_link = ['https://www.worldathletics.org/competition/calendar-results/results/',str(filtered_df_clean['id'][index]),'?day=',str(j)]
            results_url = ''.join(things_to_make_link)
            results_urls.append(results_url)
            
    return results_urls

###############################################################################

#2A - Look at the Top N Marks

#Create a list with name of each country with his ISO code 3
import pycountry
def get_iso_code():
    list_iso3 = []
    for country in pycountry.countries:
        list_iso3.append("{} ({})".format(country.name, country.alpha_3))
    
    #Replace RUS by ANA because Russian Athletics Federation was suspended in 2015.
    #Authorised Neutral Athlete (ANA) is the category under which approuved Russian athletes can compete at international competitions.
    list_iso3_ANA = list(map(lambda x: x.replace('Russian Federation (RUS)', 'Authorised Neutral Athletes (ANA)'), list_iso3))
    
    return list_iso3_ANA


