import random
import requests
#import pandas as pd
# BEFORE YOU START - RUN tor.exe !!!!

def Scraper(searchquery):

    yourquery = searchquery
    if " " in yourquery:
        yourquery = yourquery.replace(" ","+")
    
    url = "https://ahmia.fi/search/?q={}".format(yourquery) #we use ahmia.fi to gather onion links
    print(url)

    #Fake Agent gan awowkwowk
    ua_list = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19577"
    ,"Mozilla/5.0 (X11) AppleWebKit/62.41 (KHTML, like Gecko) Edge/17.10859 Safari/452.6", "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2656.18 Safari/537.36"
    ,"Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML like Gecko) Chrome/44.0.2403.155 Safari/537.36", "Mozilla/5.0 (Linux; U; en-US) AppleWebKit/525.13 (KHTML, like Gecko) Chrome/0.2.149.27 Safari/525.13","Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27"
    ,"Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_5_8; zh-cn) AppleWebKit/533.20.25 (KHTML, like Gecko) Version/5.0.4 Safari/533.20.27"]
    ua = random.choice(ua_list)
    headers = {'User-Agent': ua}

    request = requests.get(url, headers=headers) #, verify=False)
    content = request.text

    def findlinks(content):
        #ambil content - webpage dalam string format - abis itu cari make regex
        import re
        import random
        
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
        mineddata = findlinks(content)
        return mineddata

def torSearcher(url):

    def get_tor_session():
        session = requests.session()
        # Tor uses the 9050 port as the default socks port
        session.proxies = {'http':  'socks5h://127.0.0.1:9050',
                           'https': 'socks5h://127.0.0.1:9050'}
        return session

    # Make a request through the Tor connection
    # IP visible through Tor
    session = get_tor_session()

    print("Getting ...", url)
    result = session.get(url).text
    
    import string
    filename = ''.join(random.choice(string.ascii_lowercase) for i in range(16))
    with open(f"{filename}.txt","w+", encoding="utf-8") as newthing:
        newthing.write(result)

if __name__ == "__main__":
    search = input('Your Search Query Here : ')
    onions = Scraper(search)
    #print(onions)
    for onion in onions :
        try :
            url = 'http://' + onion
            torSearcher(str(url))
        except :
            print('The Onion Links Expired bruh...')