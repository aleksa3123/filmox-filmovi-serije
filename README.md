# Filmox - filmovi-serije

Skripta koja pronalazi filmove/serije i ubacuje ih u bazu podataka

1. Potrebni moduli:

pip3 install beautifulsoup4
pip3 install requests
pip3 install lxml
pip3 install colorama
pip3 install mysql-connector-python

2. Skriptu pokrecete sa python3 filmox.py
3. Izbacice vam da unesete broj page (sa koliko page zelite da uzmete sadrzaj)
4. Kada je skripta zavrsila izbacice vam "Uspesno ste sacuvali sav sadrzaj!", svi podatci koje
je skripta sakupila nalaze se u sadrzaj.json fajlu. Sledeci korak je ubacivanje podataka u bazu
5. Da bu pokrenuli insert.py morate imati modul mysql-connector-python inace vam skripta nece raditi.

