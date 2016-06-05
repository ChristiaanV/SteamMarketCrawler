import WebCrawler as wc
from time import sleep
wc.get_appids()
pageNum = int(input("Enter a game number from above "))
while(True):
    wc.display(wc.crawl_page(pageNum))
    sleep(1)