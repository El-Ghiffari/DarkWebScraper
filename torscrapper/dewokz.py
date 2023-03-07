import requests
import random
import os
import string
from bs4 import BeautifulSoup

def gambar() :
    print(".........................................................................")
    print(" ______    ________   ___                   ___      ____     ___        ")
    print("|      |  |   _____| |   |                 |   |     |   |   /   /       ")
    print("|       |  |   |      |   |      / \      |   |      |   |  /   /        ")
    print("|  __    |  |   |_____ |   |    /   \    |   |       |   | /   /         ")
    print("| |__\    |  |        \ |   |  /     \  |   |        |   |/   /          ")
    print("| |__/    |  |   _____/  |   |/.     .\|   |   ___   |       /           ")
    print("|        |  |   |         |                |  / _ \  |       \           ")
    print("|       |  |   |____       |   |\    /|   |  | (_) | |   |\   \          ")
    print("|______|  |_________|      |___| \__/ |___|   \___/  |___| \___\ ____    ")
    print("                                                                         ")
    print("      BY              _          ______      ___                         ")
    print("                     | |        |   _  \__  / _ \   __   __    _         ")
    print("                     | |_   ___ |  |_|  | |/ /_\ \ |  |_|__|  | |        ")
    print("                     | __| / _ \|   ___/  ||  _  | |  __  ||__| |        ")
    print("                     | |_ | (_) |  |   |  || | | | | |  |_|_    |        ")
    print("                      \__| \___/|__|   |__|\_| |_/ |_|  ____|   |        ")
    print(".......................................................|________|........")

def torSearcher(url):
    # BEFORE YOU START - RUN tor.exe !!!!
    # This function will scrape an onion links and their first level of directory
    # e.g /about /info etc...
    try :
        result = scraping(url)

        # get links inside a tag
        soup = BeautifulSoup(result, 'html.parser')
        tags = soup.find_all('a')
        for tag in tags :
            check = str(tag.get('href'))
            if (len(check) != 1) :
                if (check[0] == '/') :
                    linkbaru = str(url+tag.get('href'))
                    scraping(linkbaru)
    except :
        print('[ERROR] ... Please check again...')

def gettags(url) :
    # This function will collect every link inside href in  given page
    try :
        result = crawling(url)
        newtags = []
        # get links inside a tag
        soup = BeautifulSoup(result, 'html.parser')
        tags = soup.find_all('a')
        for tag in tags :
            check = str(tag.get('href'))
            if (len(check) != 1) :
                if (check[0] == '/') :
                    newtags.append(str(url+tag.get('href')))
        
        return newtags
    except :
        print('[ERROR] ... Failed to Extraxt interlinks...')


def get_tor_session():
    # Just to get  TOR Session
    try :
        session = requests.session()
        # Tor uses the 9050 port as the default socks port
        session.proxies = {'http':  'socks5h://127.0.0.1:9050',
                           'https': 'socks5h://127.0.0.1:9050'}
        return session
    except :
        return 0

def crawling(url) :
    # Crawl the Given URL but not scrpe it
    try :
        session = get_tor_session()
        print('[INFO] ... CRAWL FOR DEEPER LINKS')
        result = session.get(url).text
        return result
    except :
        print('[FATAL] ... IT SEEMS SOMETHING WENT WRONG HERE...')

def scraping(url) :
    # Scrap the onion site nd save it into html files
    # IP visible through Tor
    try :
        session = get_tor_session()
        print("[INFO] Scraping ...", url)
        result = session.get(url).text
        
        # Create a directory named 'results' if it doesn't exist
        if not os.path.exists('results'):
            os.makedirs('results')
        filename = ''.join(random.choice(string.ascii_lowercase) for i in range(16))
        #filename = str(url)
        with open('results/'f"{filename}.html","w+", encoding="utf-8") as newthing:
            newthing.write(result)
        return result
    except :
        print('[ERROR] ... IT SEEMS WE CANNOT SCRAPE THE LINK ...')

if __name__ == "__main__":
    gambar()
    url = "http://grqwuipwwfuu5mkyyqfea32kbkvwvxm36hau6bvkzoozchf57moj6yqd.onion" 
    torSearcher(url)
    try :
        urlbaru = gettags(url)
        print('[INFO] ... INITIATE DEEP CRAWLING !!!')
        for tag in urlbaru :
            print('[INFO] ... GETTING ', tag)
            torSearcher(tag)
    except :
        print('[FINISH] ... TERMINATE THE PROCESSES')

    
