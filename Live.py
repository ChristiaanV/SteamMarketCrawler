import ConsoleDisplay as cd
from time import sleep

cd.display_appids()
pageNum = int(input("\nEnter a game number from above "))

while(True):
    cd.display(pageNum)
    sleep(1)