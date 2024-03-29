import requests
import random
import os
import string
from bs4 import BeautifulSoup

# BEFORE YOU START - RUN tor.exe !!!!

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
    print("|______|  |_________|      |___| \__/ |___|   \___/  |___| \___\ _______ ")
    print("                                                                         ")
    print("      BY              _          ______      ___                         ")
    print("                     | |        |   _  \__  / _ \   __    _    _         ")
    print("                     | |_   ___ |  |_|  | |/ /_\ \ |  |__| |  | |        ")
    print("                     | __| / _ \|   ___/  ||  _  | |  __  ||__| |        ")
    print("                     | |_ | (_) |  |   |  || | | | | |  |_|__   |        ")
    print("                      \__| \___/|__|   |__|\_| |_/ |_|  _____|  |        ")
    print(".......................................................|________|........")

def torSearcher(url):
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

def torSearcherGreed(url, depth) :
    # This function will scrapped recursively using depth as a flag
    result = scraping(url)

    # get links inside a tag
    if (depth != 1) :
        soup = BeautifulSoup(result, 'html.parser')
        tags = soup.find_all('a')
        for tag in tags :
            check = str(tag.get('href'))
            if (len(check) != 1) :
                if (check[0] == '/') :
                    linkbaru = str(url+tag.get('href'))
                    torSearcherGreed(linkbaru, (depth-1))
    elif (depth < 1) :
        print('[INFO] ... Depth Value cannot be 0 or Lower ...')
    else :
        print('[INFO] ... DONE SCRAPING ...')

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

def Scraper(searchquery):
    # This function are scraping onion links from ahmia.fi and other search engines
    contents = 'start here : \n'
    yourquery = searchquery
    if " " in yourquery:
        yourquery = yourquery.replace(" ","+")
    
    # url = "https://ahmia.fi/search/?q={}".format(yourquery) # we use ahmia.fi to gather onion links
    # print(url)
    urls = ["http://search7tdrcvri22rieiwgi5g46qnwsesvnubqav2xakhezv4hjzkkad.onion/result.php?search={}",
            "http://juhanurmihxlp77nkq76byazcldy2hlmovfu2epvl5ankdibsot4csyd.onion/search/?q={}",
            "http://haystak5njsmn2hqkewecpaxetahtwhsbsa64jom2k22z5afxhnpxfid.onion/?q={}",
            "http://oniondxjxs2mzjkbz7ldlflenh6huksestjsisc3usxht3wqgk6a62yd.onion/search?query={}",
            "http://tordexu73joywapk2txdr54jed4imqledpcvcuf75qsas2gwdgksvnyd.onion/search?query={}"] #we use ahmia.fi and other search engines to gather onion links
    for url in urls:
        print("[INFO] ... Gathering Onion from : ", url.format(yourquery))
        url = url.format(yourquery)
        #Fake Agent gan awowkwowk
        ua_list = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19577"
        ,"Mozilla/5.0 (X11) AppleWebKit/62.41 (KHTML, like Gecko) Edge/17.10859 Safari/452.6", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2656.18 Safari/537.36"
        ,"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36", "Mozilla/5.0 (Linux; U; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13","Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27"
        ,"Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; zh-cn) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27"]
        ua = random.choice(ua_list)
        headers = {'User-Agent': ua}
        session = get_tor_session()
        request = session.get(url, headers=headers) #, verify=False)
        content = request.text
        contents = contents + content

    def findlinks(content):
        #ambil content - webpage dalam string format - abis itu cari make regex
        import re
        #import random
        
        regexquery = "\w+\.onion"
        #regex query buat nyari pattern onion links
        mineddata = re.findall(regexquery, content)

        #n = random.randint(1,9999)
        
        filename = "sites{}.txt".format(str(yourquery))
        print("Saving to ... ", filename)
        mineddata = list(dict.fromkeys(mineddata))
        
        with open(filename,"w+") as _:
            print("")
        for k in mineddata:
            with open(filename,"a") as newfile:
                k  = k + "\n"
                newfile.write(k)
        print("All the files written to a text file : ", filename)
        return mineddata


    if request.status_code == 200:
        print("Request went through. \n")
        #print(content)
        mineddata = findlinks(contents)
        return mineddata
    
def scrapahmia(url) :
    # To Scrap the onion site generated by ahmia, it will only scrap the main page
    session = get_tor_session()
    print("[INFO] Getting ...", url)
    result = session.get(url).text
    filename = ''.join(random.choice(string.ascii_lowercase) for i in range(16))
    # Create a directory named 'results' if it doesn't exist
    if not os.path.exists('results'):
        os.makedirs('results')
    with open('results/'f"{filename}.html","w+", encoding="utf-8") as newthing:
        newthing.write(result)

if __name__ == "__main__":
    gambar()
    print('[OPTION] #1 : Scrap and Crawl specific website')
    print('[OPTION] #2 : Scrap and Crawl specific website recursively')
    print('[OPTION] #3 : Gather onion links based on your search Query')
    print('[OPTION] #4 : Gather onion links based on your search Query and Scrap them')
    options = input('Your Options : ')
    if (options == '1') :
        url = input('Your onion link : ')
        if 'http://' in url :
            torSearcher(url)
        else :
            url = 'http://' + url
            torSearcher(url)
        try :
            urlbaru = gettags(url)
            print('[INFO] ... INITIATE DEEP CRAWLING !!!')
            for tag in urlbaru :
                print('[INFO] GETTING ', tag)
                torSearcher(tag)
        except :
            print('[FINISH] ... TERMINATE THE PROCESSES')
    elif (options == '2') :
        depth = input('How deep you want to crawl : ')
        url = input('Your onion link : ')
        if 'http://' in url :
            torSearcherGreed(url, int(depth))
        else :
            url = 'http://' + url
            torSearcherGreed(url, int(depth))
        #url = "http://grqwuipwwfuu5mkyyqfea32kbkvwvxm36hau6bvkzoozchf57moj6yqd.onion" 
    elif (options == '3') :
        search = input('Your Search Query Here : ')
        onions = Scraper(search)
    elif (options == '4') :
        search = input('Your Search Query Here : ')
        onions = Scraper(search)
        #print(onions)
        for onion in onions :
            try :
                url = 'http://' + onion
                scrapahmia(str(url))
            except :
                print('[INFO] The Onion Links Expired bruh...')
    else :
        print('[ERROR] ... Choose the Correct Options pleaseee...')

    
