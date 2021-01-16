import requests
import json
import textwrap
import base64

from bs4 import BeautifulSoup
from colorama import Fore, Back, Style


filmox = """
______ _ _                     
|  ___(_) |                    
| |_   _| |_ __ ___   _____  __
|  _| | | | '_ ` _ \ / _ \ \/ /
| |   | | | | | | | | (_) >  < 
\_|   |_|_|_| |_| |_|\___/_/\_\\
                                                                                                  
VenoxZero je radio traku!
"""
print(Fore.RED + filmox )
broj = input(Fore.YELLOW + 'Unesite broj strana: ') #Input za unosenje broja stranica

stranice = int(broj) + 1 #Dodavanje 1 na broj stranica da bi broj bio tacan

def write_json(data,filename="sadrzaj.json"): #Definisanje json fajla
    with open(filename, "w") as f: 
        json.dump(data, f,  indent=4)


with open("sadrzaj.json") as json_file: #Otvaranje json fajla
    data = json.load(json_file) #Ocitavanje podataka iz json fajla

    

    for i in range(1, int(stranice)):#For loop za broj stranica

        URL = 'https://www.popcornsrbija.com/filmovi/?page=' + str(i) #URL sa kog su stranice, njega mozete menjati ali paginacija mora biti preko get metode(Ako je ?page drugacije promenite ga)
        page = requests.get(URL)

        soup = BeautifulSoup(page.content, 'html.parser')


        for opis in soup.find_all('div', class_='opis'): #Pronalazi sve div tagove sa klasom opis
            title =  opis.find('a')
            link = 'https://www.popcornsrbija.com' + title['href'] #Pravljenje linka za film
            page = requests.get(link)

            soup = BeautifulSoup(page.content, 'html.parser')
           

            results = soup.find('body')

            #Definisanje promenljivih
            title = results.find('h1')
            opis = results.find('p')
            iframe = results.find('iframe')
            temp = data["filmovi"]
            
            naslov = title.text
            naslov_r = naslov[:naslov.find('(')].strip()


            #Ubacivanje podataka u json fajl
            y = {
                
            "url" : link ,
            "naslov": str(naslov_r),
            "opis": str(opis.text),
            "iframe": str(iframe)
            
            }

            temp.append(y)
            print(naslov_r)
            

write_json(data)
print("\n")
print("Uspesno ste sacuvali sav sadrzaj!")
