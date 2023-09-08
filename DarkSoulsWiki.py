

import requests
from bs4 import BeautifulSoup
#import re
#import time
import urllib
from urllib.request import urlopen

#import webbrowser
#======================================================================================================================================================
print("Welcome to my scuffed webcrawler!")
print("")
print("Use ConnectedLinks('https://darksouls3.wiki.fextralife.com/') to view the organized webcrawler")
print("   -This takes a LOT of time, around 20 - 25 min")
print("   -I am currently working on this part to make it better, faster, and more reliable")
print("   -This was made so that  I could practice scraping a website with python, and then sort through the data based on how the website was set up.\nFor this reason, this will only work on the dark souls wiki and not any other wiki, because it gets rid of some data based on how the fextralife wiki is set up")
print("")
#======================================================================================================================================================

#use webbrowser.open(url,new =1), new = 0 opens in same browser window,
#new = 1 opens a new browser window, new = 2 opens in a new tab

found = False
weapon = 0
armour = 0
misc = 0
spells = 0
none = 0
issue = 0
total = 0

checklinkList = ["/Miracles","/Pyromancies","/Sorceries",
                     "/Weapons","/Shields","/Armor","/Helms",
                     "/Chest+Armor","/Gauntlets","/Leg+Armor","/Rings"]
def FinalSort(classification,item):
    global found
    global weapon
    global spells
    global armour
    global total
    global none
    global issue

    
    if classification == "Weapon":
        weapon = weapon +1
    elif classification == "Spells":
        spells = spells + 1
    elif classification == "Armor":
        armour = armour + 1
    elif classification == "Issue":
        issue = issue + 1
    else:
        none = none+1
    total = total + 1
    if total > 1215:
        print(item)
    print(total)
    found = True

#gets all items
def ConnectedLinks(website):
    
    #keeps track of visited sites
    allLinks = set()

    #creates website instance
    response = requests.get(website)
    responded = response.text
    soup = BeautifulSoup(responded,'html.parser')
    
    for deeperLinks in soup.find_all('a', href = True):
        deeperLinks = deeperLinks['href']
        if deeperLinks in checklinkList:
            if len(deeperLinks) != 0:
                if deeperLinks[0] == "/":
                    deeperLinks = "https://darksouls3.wiki.fextralife.com" + deeperLinks
                if deeperLinks[:39] == "https://darksouls3.wiki.fextralife.com/":
                    allLinks.add(deeperLinks)
    #print(allLinks)
    
    deepdive = set()
    while True:
        try:
            for deeperLinks in allLinks:
                response = requests.get(deeperLinks)
                responded = response.text
                soup = BeautifulSoup(responded,'html.parser')
                
                for link in soup.find_all('a', href = True):
                    FORUM = str(link.get('href'))
                    
                    if FORUM[:29] != 'https://fextralife.com/forums':
                        deepdive.add(str(link.get('href')))
                        #print(str(link.get('href')))

        except Exception as e:
            continue
        break
    #Print out all links found in a list
    deepdive.remove("")
    print(deepdive)
    print(len(deepdive))
    SortLinks(deepdive)

#======================================================================================================================================================
#Sort the links found in ConnectedLinks into categories based on the text present in the body of each link
def SortLinks(usedlist):
    global found
    global weapon
    global spells
    global armour
    global total
    global none
    global misc
    global issue
    
    checkThis = ["Weapon","Sorcery","Pyromancy","Miracle","Armor"]
    
    finalReturn = {"W":"Weapon","S":"Spells","P":"Pyromancy",
                   "M":"Miracle","A":"Armor"}
    
    attachment = "https://darksouls3.wiki.fextralife.com"
    countertime = 0

    #Visit each link and seperate the main body text into a variable
    for item in usedlist:
        found = False
        try:
                if countertime < 11:
                    print(item)
                    
                countertime+=1
        
                
                url = attachment + str(item)

                html = urllib.request.urlopen(url).read()
                soup = BeautifulSoup(html, features="html.parser")
                # kill all script and style elements
                
                for script in soup(["script", "style"]):
                    script.extract()   

                # get text
                text = soup.get_text()

                # break into lines and remove leading and trailing space on each
                lines = (line.strip() for line in text.splitlines())
                # break multi-headlines into a line each
                chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
                # drop blank lines
        
                text = '\n'.join(chunk for chunk in chunks if chunk)
                #print("\n" + text)
            
                    #returns a massive chunk of raw string, not individual words
                    #THIS WORKS TO GIVE LINE CONTAINING DESCRIPTION
                    
           
                
                newword = ""
                word2 = ""
                WhatitIs = ""
                check = False
                y = 100
    
                #parse the text into sections of text
                
                counter = 0
                counterword = 0
               
                words = text.split()

                #Spells and Armor works, not weapons, shields, rings, etc
                placeholder = ""
              

                #This is meant to find identifying factor
                for word in words:
                    try:
                        if word == "Type":
                        
                            FinalSort(finalReturn[placeholder[0]],item)
                            #usedlist.remove(item)
                            break
                        elif word == "Weapons" or word == "Soul Transposition":
                            if placeholder == '/':
                                FinalSort(finalReturn[word[0]],item)
                                #usedlist.remove(item)
                                break
                        elif word == "Shields":
                            if placeholder == '/':
                                FinalSort(finalReturn["A"],item)
                                #usedlist.remove(item)
                                break
                        else:
                            placeholder = word
                        
                    except Exception as e:
                        print("ISSUE:|>>>>>>|")
                        print(item)
                        print(e)
                        FinalSort("None",item)
                        break
                        #continue
                if found == False: 
                    FinalSort("None",item)  
                        
                
                
                        
        except Exception as e:
            #print("DONE")
            #break
            FinalSort("Issue",item)
            continue
        #break
    print('Weapon = ' + str(weapon))
    print('Armor = ' + str(armour))
    print('Misc = ' + str(misc))
    print('Spells = ' + str(spells))
    print('None = ' + str(none))
    print('Issue = ' + str(issue))
    print('total = ' + str(total))
#ConnectedLinks("https://darksouls3.wiki.fextralife.com/")
#time.sleep(3)
ConnectedLinks("https://darksouls3.wiki.fextralife.com/")
#======================================================================================================================================================
