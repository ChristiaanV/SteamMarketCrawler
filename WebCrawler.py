import requests
from bs4 import BeautifulSoup


def crawl_page(gameNum):
    """Crawls the first page of the steam market for the game with appid = gameNum (eg. CS:GO is 730) """
    
    url = "http://steamcommunity.com/market/search?appid="+str(gameNum)
    page = requests.get(url).text
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
    """Returns all the games and their appids in a list ([[game 1 name, game 1 id],...])"""    
    
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