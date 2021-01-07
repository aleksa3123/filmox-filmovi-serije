import mysql.connector
import json
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
host_input = input(Fore.YELLOW + 'Unesite ip adresu databaze: ')
user_input = input(Fore.YELLOW + 'Unesite korisnicko ime: ')
passwd_input = input(Fore.YELLOW + 'Unesite sifru: ')
database_input = input(Fore.YELLOW + 'Unesite ime baze: ')




mysql=mysql.connector.connect(
    host = host_input, 
    user = user_input, 
    passwd = passwd_input,
    database = database_input

)
with open('sadrzaj.json') as json_file:
    data = json.load(json_file)
    for p in data['filmovi']:
        naslov = p['naslov']
        iframe = p['iframe']
        opis = p['opis']
        mycursor = mysql.cursor()
        sql = "INSERT INTO filmovi(naslov, iframe, opis) values(%s,%s, %s)"
        val = (naslov, iframe, opis)

        mycursor.execute(sql,val)

mysql.commit();




