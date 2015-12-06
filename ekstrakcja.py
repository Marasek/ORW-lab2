#-*- coding: utf-8 -*-
import urllib, re, time
# urllib jest czescia standardowej biblioteki Pythona. Zawiera on funkcje służące do pobierania informacji o danych, a także pobierania samych danych z internetu
#najwiekszym zastosowanie dla re jest poszukiwanie tekstow
# time potrzebne jest do manipulowania godzinami i datami
url = urllib.urlopen('http://www.meteoprog.pl/pl/weather/Libiaz/')
url_tekst = url.read()
 
wyrazenie = '<meta property="og:description" content="(.+?)" />' #18 linia
pogoda = re.findall(wyrazenie, url_tekst) #zwraca wszystkie pary zapisujac je w ciag, lista pasujacych wzorcow
 
wyrazenie2 = 'd</span><span class="colorNoBold">(.+?)</span>' #1184 linia
wschodzachod = re.findall(wyrazenie2, url_tekst)
 
print time.strftime("%Y-%m-%d, %H:%M:%S") #zwraca lancuch znakow reprezentujacy date i godzine
print '-' * 20
print pogoda[0]
print u'Wschód słońca', wschodzachod[0]
print u'Zachód słońca', wschodzachod[1]
print u'Długość dnia', wschodzachod[2]
