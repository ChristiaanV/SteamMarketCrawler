import WebCrawler as wc
from time import sleep

while(True):
    wc.display(wc.crawl_page(570))
    sleep(1)