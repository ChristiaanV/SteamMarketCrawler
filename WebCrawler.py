import requests
from bs4 import BeautifulSoup
import os
#import urllib2

def crawl_page(gameNum):
    url = "http://steamcommunity.com/market/search?appid="+str(gameNum)
    page = requests.get(url).text
    #page = urllib2.urlopen(url)
    soup = BeautifulSoup(page,'html.parser')
    
    names=[]
    for link in soup.findAll('span', {'class': 'market_listing_item_name'}):
        names.append(link.string)        
    quantity=[]
    for link in soup.findAll('span', {'class': 'market_listing_num_listings_qty'}):
        quantity.append(link.string)
    price=[]
    for link in soup.findAll('span', {'class': 'normal_price'}):
        if (link.string != None):        
            price.append(link.string)    
    result = []
    for i in range(len(names)):
        result.append([names[i],quantity[i],price[i]])
    return result
    
def get_appids():
    url = "http://steamcommunity.com/market/"
    page = requests.get(url).text
    soup = BeautifulSoup(page,'html.parser')
    
    names=[]
    for link in soup.findAll('span', {'class': 'game_button_game_name'}):
        names.append(link.string) 
        
    appid=[]
    for link in soup.findAll('a', {'class': 'game_button'}):
        appid.append(link.get('href'))
        
    results = []
    for i in range(len(names)):
        results.append([names[i],appid[i]])
    return results

def display_appids():    
    clear = lambda:os.system('cls')
    clear()
    Results = get_appids()
    for k in range(len(Results)):
        name =  str(Results[k][0]).replace("\t","").replace("\n","").replace("\r","")
        appid = str(Results[k][1]).replace("http://steamcommunity.com/market/search?appid=","").replace("\t","").replace("\n","").replace("\r","")
        print name + " (" + appid + ")"

def display(crawlData):
    clear = lambda:os.system('cls')
    clear()
    print("Quantity\tPrice\tName\n")
    Results = crawlData
    for k in range(len(Results)):
        print(str(Results[k][1])+"\t"+str(Results[k][2]).replace(" USD","")+"\t"+str(Results[k][0]))
        
display_appids()