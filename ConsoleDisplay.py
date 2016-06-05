import WebCrawler as wc
import os


def display_appids():
    """Calling this def will print all the games with their appids in the console"""    
    
    clear = lambda:os.system('cls')
    clear()
    Results = wc.get_appids()
    for k in range(len(Results)):
        name =  str(Results[k][0]).replace("\t","").replace("\n","").replace("\r","")
        appid = str(Results[k][1]).replace("http://steamcommunity.com/market/search?appid=","").replace("\t","").replace("\n","").replace("\r","")
        print name + " (" + appid + ")"

def display(appID):
    """Calling this def will print the top ten most popular items, amount available and current price """
    
    crawlData = wc.crawl_page(appID)
    if(len(crawlData )!= 0):
        clear = lambda:os.system('cls')
        clear()
        print("Amount\tPrice\tName\n")
        Results = crawlData
        for k in range(len(Results)):
            print(str(Results[k][1])+"\t"+str(Results[k][2]).replace(" USD","")+"\t"+str(Results[k][0]))