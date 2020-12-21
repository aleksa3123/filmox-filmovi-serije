import requests
from bs4 import BeautifulSoup

broj = input('Unesite broj strana: ')
text_file = open("linkovi.txt", "w")
for i in range(1, int(broj)):

    URL = 'https://www.popcornsrbija.com/?page=' + str(i)
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, 'html.parser')


    for opis in soup.find_all('div', class_='opis'):
        title =  opis.find('a')
        print ('https://www.popcornsrbija.com' + title['href'])
        text_file.write('https://www.popcornsrbija.com' + title['href'] + '\n')

text_file.close()





 
 