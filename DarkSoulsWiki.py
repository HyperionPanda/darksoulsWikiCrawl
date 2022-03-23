
#use webbrowser.open(url,new =1), new = 0 opens in same browser window,
#new = 1 opens a new browser window, new = 2 opens in a new tab

import requests
from bs4 import BeautifulSoup
import re
import urllib
from urllib.request import urlopen

import webbrowser

#======================================================================================================================================================

print("Welcome to my scuffed webcrawler!")
print("")
print("Use ConnectedLinks(website) to find all the connected links of a particular website")
print("   -This is not all links of a website, just the immediate links connected to the given one")
print("")
print("Currently not active (or working) below")
print("Use SoupCheck('https://darksouls3.wiki.fextralife.com/') to view the organized webcrawler")
print("   -This takes a LOT of time")
print("   -I am currently working on this part to make it better, faster, and more reliable")
print("")

#======================================================================================================================================================


def ConnectedLinks(website):

    #keeps track of visited sites
    doNotUseLinks = set()

    #creates website instance
    response = requests.get(website)
    responded = response.text
    soup = BeautifulSoup(responded,'html.parser')

    for deeperLinks in soup.find_all('a', href = True):
        deeperLinks = deeperLinks['href']
        if len(deeperLinks) != 0:
            if deeperLinks not in doNotUseLinks:
                doNotUseLinks.add(deeperLinks)
                print(deeperLinks)

#======================================================================================================================================================
                
'''
# Meant for Dark Souls wiki, gets rid of useless link
def SoupCheck(website):

    newword = ""
    word2 = ""
    WhatitIs = ""
    #website = input("Please give a url: ")
    
    #initial creation of website to parse through
    response = requests.get(website)
    responded = response.text
    soup = BeautifulSoup(responded,'html.parser')

    #list meant to organize and check for different items
    checklinkList = ["/Miracles","/Pyromancies","/Sorceries",
                     "/Weapons","/Shields","/Armor","/Helms",
                     "/Chest+Armor","/Gauntlets","/Leg+Armor","/Rings"]
    
    doNotUseLinks = set()
    #Link that appears to break code
    doNotUseLinks.add("https://darksouls3.wiki.fextralife.com/Talismans+")

    itemDict = {}
    keyForDict  = ""
    #for each link, compile the items in the main links and organize into a list
    for theLINKS in soup.find_all('a', href = True):
        
        if theLINKS['href'] in checklinkList:
            
            keyForDict = theLINKS['href']
            #create a usable link
            link =  "https://darksouls3.wiki.fextralife.com" + theLINKS['href']
            
            response2 = requests.get(link)
            responded2 = response2.text
            newsoup = BeautifulSoup(responded2,'html.parser')

            listForDict = []
            
            for deeperLinks in newsoup.find_all('a', href = True):
                deeperLinks = deeperLinks['href']
                if len(deeperLinks) != 0:
                    if deeperLinks[0] == "/":
                        deeperLinks = "https://darksouls3.wiki.fextralife.com" + deeperLinks
                if deeperLinks not in doNotUseLinks:
                    doNotUseLinks.add(deeperLinks)
                    if deeperLinks[:39] == "https://darksouls3.wiki.fextralife.com/":
                        print(deeperLinks)
    print(len(doNotUseLinks))
            
        
   
            


#======================================================================================================================================================

# Meant for checking Dark Souls wiki to see weapon types
def ChecktheType(website):
    
    checkThis = ["Weapon","Sorcery","Pyromancy","Miracle","Armor"]
    finalReturn = {"W":"Weapon","S":"Sorcery","P":"Pyromancy",
                   "M":"Miracle","A":"Armor"}

    url = website
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
    #print(text)

    #!!!!!!!!
    #returns a massive chunk of raw string, not individual words, figure out how to split

    #THIS WORKS TO GIVE LINE CONTAINING DESCRIPTION
    #print("got Here")
    newword = ""
    word2 = ""
    WhatitIs = ""
    check = False
    y = 100
    
    #parse the text into sections of text
    for Individualwords in text:
        if Individualwords == "\n":
            
            if check:
                
                newword = newword[10:]
                for a in checkThis:
                    #this is the start of the necessary word
                    x = newword.find(a)
                    if x > 0 and x < y:
                        y = x
                check = False
                break
            
            else:
                if newword == "+":
                    check = True
            newword = ""
        else:
            newword = newword + Individualwords
    
    if y == 100:
        return ""
    else:
        return finalReturn[newword[y]]
    
    

#SoupCheck("https://darksouls3.wiki.fextralife.com/")
#AllLinks("https://darksouls3.wiki.fextralife.com/")

'''




#SoupCheck before major changes
'''
def SoupCheck(website):

    newword = ""
    word2 = ""
    WhatitIs = ""
    check = False
    #website = input("Please give a url: ")
    
    #initial creation of website to parse through
    response = requests.get(website)
    responded = response.text
    soup = BeautifulSoup(responded,'html.parser')

    #list meant to organize and check for different items
    checklinkList = ["/Miracles","/Pyromancies","/Sorceries",
                     "/Weapons","/Shields","/Armor","/Helms",
                     "/Chest+Armor","/Gauntlets","/Leg+Armor","/Rings"]
    doNotUseLinks = set()
    

    itemDict = {}
    keyForDict  = ""
    #for each link, compile the items in the main links and organize into a list
    for theLINKS in soup.find_all('a', href = True):
        
        if theLINKS['href'] in checklinkList:
            
            keyForDict = theLINKS['href']
            #create a usable link
            link =  "https://darksouls3.wiki.fextralife.com" + theLINKS['href']
            
            response2 = requests.get(link)
            responded2 = response2.text
            newsoup = BeautifulSoup(responded2,'html.parser')

            listForDict = []
            
            for deeperLinks in newsoup.find_all('a', href = True):
                deeperLinks = deeperLinks['href']
                if len(deeperLinks) != 0:
                    if deeperLinks[0] == "/":
                        deeperLinks = "https://darksouls3.wiki.fextralife.com" + deeperLinks
                if deeperLinks not in doNotUseLinks:
                    
                    doNotUseLinks.add(deeperLinks)
                    if deeperLinks[:39] == "https://darksouls3.wiki.fextralife.com/":
                        print(deeperLinks)
                        typeOFLINK = ChecktheType(deeperLinks)
                        if ("/"+typeOFLINK) == keyForDict:
                            listForDict.append(deeperLinks)
                        else:
                            doNotUseLinks.discard(deeperLinks)
            print(listForDict)           
            itemDict[keyForDict] = listForDict
    print(" ")
    print(itemDict)
'''
