import requests
from bs4 import BeautifulSoup

URL = input('Ukucajte url sajta: ')
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

results = soup.find('body')


naslov = results.find('h1')
opis = results.find('p')
iframe = results.find('iframe')
print(naslov.text)
print("\n")
print(opis.text)
print("\n")
print(iframe)

 
 