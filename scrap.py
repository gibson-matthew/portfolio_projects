# WELCOME TO SCRAP.PY!
import urllib.request,  urllib.parse, urllib.error
import ssl
import re
from bs4 import BeautifulSoup as bs
import time

class Messages():
    def welcome():
        welcome = """
====================================
       WELCOME TO SCRAP.PY!
------------------------------------
Enter website with any format:
>> https://www.google.com/
>> www.google.com/
>> google.com/
------------------------------------
       Enter '?' for help!
====================================
"""
        print(welcome)

    def help():
        objective = """
===========================================================================================================================
                                               SCRAP.PY'S OBJECTIVE:
To create a web-scraper in python (scrap.py, haha), purposed for retrieving, parsing, organizing, and storing desired data.
---------------------------------------------------------------------------------------------------------------------------
SCRAP.PY's THREE STEP PROCESS:
>> Enter URL                        (example: https://www.google.com/)
>> Choose data retrieval method     (word count, link finder, etc.)
>> Export data to desired location  (personal computer, AWS S3 Bucket, etc.)
===========================================================================================================================
"""
        print(objective)

# Loop for url attempts
class Urls():
    count = 0 # Count to show # of tabs open
    key_dict = {}    

    def __init__(self, link):
        self.link = link 
    
    #def url_clean(): makes url into valid format
   
    def connection(self):
        url = f"{self.link}" 
        print('Creating connection to', url)
        print(Fancy.loading())

        # Ignores SSL certificate
        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE
        print(' >> Hostname valid\n' + ' >> Certificate valid')
       
        # Establishes connect / creates GET request / encodes data into bytes / stores page into 'HTML' object
        try: 
            page = urllib.request.urlopen(url, context=ctx).read()
            Urls.count = Urls.count + 1 # increases count 
            Urls.Keys(page) # Adds page to key_dict dictionary
            time.sleep(1)
            print('SUCCESS') 
        except:
            time.sleep(1)
            print('FAILURE')

    # SETS KEY / LINK VALUES
    def Keys(page):
        tab = 'tab'
        key = tab + str(Urls.count)
        Urls.key_dict.update({key:page})
        print(key)
        

# Establishing connection / stores in open_tabs DICT
class Tabs(Urls):
    # Construction
    def __init__(self, key, data):
        self.key = key
        self.data = data
        # Shows class contruction
        print('[', end='')
        time.sleep(.05)
        for x in range(1,25):
            print('=', end='')
            time.sleep(.05)
        print(']')

    # Methods
    #def tab_creation(self):
        
# Parsing options
# class Parsers():

# Adds fancy effects to SCRAP.PY!
class Fancy():
    # Class for some fancy effects!
    def loading():
        print('[', end='')
        time.sleep(.05)
        for x in range(1,25):
            print('=', end='')
            time.sleep(.05)
        print(']')
        return 'SSL validity:'

# Start of SCRAP.PY!
Messages.welcome() # Welcome message

# Loop for welcome page or break to continue
while True:
    print('loop on')
    link = input('Desired connection: ')
    if link == '?':
        Messages.help()
    else:
        break

print('look broke')

# Add loop for incorrect link
# Add tab visuals
# Add open tab list
# Add parsing capabilities 

instance = Urls(link)

instance.connection()
