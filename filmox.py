import requests
import json
from bs4 import BeautifulSoup
import textwrap
import base64

venoxzero = """

 __      __                   ______              
 \ \    / /                  |___  /              
  \ \  / /__ _ __   _____  __   / / ___ _ __ ___  
   \ \/ / _ \ '_ \ / _ \ \/ /  / / / _ \ '__/ _ \ 
    \  /  __/ | | | (_) >  <  / /_|  __/ | | (_) |
     \/ \___|_| |_|\___/_/\_\/_____\___|_|  \___/ 
                                                  
                                                  

"""
print(venoxzero)
broj = input('Unesite broj strana: ')

stranice = int(broj) + 1

def write_json(data,filename="sadrzaj.json"):
    with open(filename, "w") as f:
        json.dump(data, f,  indent=4)


with open("sadrzaj.json") as json_file:
    data = json.load(json_file)

    

    for i in range(1, int(stranice)):

        URL = 'https://www.popcornsrbija.com/filmovi/?page=' + str(i)
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, 'html.parser')


        for opis in soup.find_all('div', class_='opis'):
            title =  opis.find('a')
            link = 'https://www.popcornsrbija.com' + title['href']
            print (link)

            page = requests.get(link)

            soup = BeautifulSoup(page.content, 'html.parser')
           

            results = soup.find('body')


            naslov = results.find('h1')
            opis = results.find('p')
            iframe = results.find('iframe')
            temp = data["filmovi"]

            message_bytes = iframe.encode('ascii')
            base64_bytes = base64.b64encode(message_bytes)
            base64_iframe = base64_bytes.decode('ascii')

            y = {
                
            "url" : link ,
            "naslov": str(naslov.text),
            "opis": str(opis.text),
            "iframe": str(base64_iframe)
            
            }

            temp.append(y)

            print(naslov.text)
            print("\n")
            #print(opis.text)
            print (opis.text)

            print("\n")
            print(base64_iframe)

write_json(data)








        






 
 