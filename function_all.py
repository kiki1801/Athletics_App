#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 19 11:33:18 2022

@author: kyllian
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

#Function to scrap 
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




