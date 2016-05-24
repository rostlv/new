__author__ = 'RLV'

from selenium import webdriver
#from bs4 import BeautifulSoup
import time
import os
import requests


# Settiamo il profile
profile = webdriver.FirefoxProfile()
profile.set_preference('browser.download.folderList', 2) # 2 per inserire il nostro path desiderato
profile.set_preference('browser.download.manager.showWhenStarting' , False) #nascondi il download file manager
profile.set_preference('browser.download.dir', os.getcwd()) #salva nella directory che vogliamo
#!!! OPPURE salva nella working directory:
#profile.set_preference('browser.download.dir', 'C:\Users\Proprietario19\Desktop\As' )
profile.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/plain, application/vnd.ms-excel, text/csv, text/comma-separated-values, application/octet-stream') #per questi tipo di file evita di chiedermi cosa farci ogni volta

browser = webdriver.Firefox(firefox_profile=profile) #apriamo il webdriver con le nostre impostazioni


#!Banca Aletti webscraping from BeautifulSoup4
#Impostiamo gli url:
url_sg = 'https://it.warrants.com/' #Societe-Generale
url_bnp = 'https://www.prodottidiborsa.com/ITA/certificati/bonus-certificates' # BNP Paribas
url_cb = 'http://www.borsa.commerzbank.com/Products/ProductSearchAdvanced.aspx?pc=5515&ex=10&c=2200207'#CommerzBank
url_imi = 'https://www.bancaimi.prodottiequotazioni.com/Prodotti-e-Quotazioni/Certificati-a-capitale-condizionatamente-protetto/Bonus' #Banca IMI
url_db = 'https://www.xmarkets.db.com/IT/Catalogo_Prodotti/Bonus_Certificate?ref=pl#&&/wEXAQUCZGYFBHRydWXegZCgVZRm2k4A3hrVqNvKzU3eqQ==' #Deutsche Bank
url_ucg = 'http://www.investimenti.unicredit.it/tlab2/it_IT/quotazioni/bonus/prezzibonusall.jsp?idNode=2470&idSite=it_IT' #Unicredit Group
# mancano Goldman Sachs (no sito), RBS (ripresa da BNP), [ING Bank, JP Morgan Structured,
# Macquaire Structured Prod, Morgan Stanley, Natixis Structured] aggiungere colonna : info mancanti

#Impostiamo gli xpath degli elementi del sito (ottenuti tramite l'ispezione degli elementi con FireBug)
xpath_sg= '/html/body/div[1]/div[2]/div[1]/div[2]/div[2]/div/div/div[2]/p[2]/a' #SG
xpath_bnp0= '/html/body/form/div[6]/div[2]/div/div[3]/a[2]'
xpath_bnp1= '/html/body/form/div[5]/table/tbody/tr[2]/td[1]/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/input[1]'
xpath_bnp2= '/html/body/form/div[5]/table/tbody/tr[2]/td[1]/div/div/div[2]/div[2]/div[2]/div[2]/div/div/div[2]/input[2]' #BNP
xpath_cb='/html/body/div[1]/form/div[6]/div[2]/div/div[2]/div/div[2]/h1/span/span/input[1]' #CommerzBank
xpath_imi0='/html/body/div[2]/div/div/div[3]/div/div[1]/button'
xpath_imi1='/html/body/div[1]/main/div[2]/section[1]/div/div[2]/div[1]/a' 
xpath_db0='/html/body/form/div[6]/div[2]/div/div/div[2]/div/div[1]/div/a[2]'
xpath_db1='/html/body/form/div[5]/div/div/div[2]/div[2]/div[1]/div[3]/div[3]/div/div[1]/div/span[1]/div/a'
xpath_db2='/html/body/form/div[5]/div/div/div[2]/div[2]/div[1]/div[3]/div[3]/div/div[1]/div/span[1]/div/div/ul/li[5]/a'
xpath_ucg0='/html/body/div[1]/div[3]/div/button'
xpath_ucg1='/html/body/div[2]/div[3]/div[2]/div[2]/div[3]/div[1]/div[2]/a'

#SOCIETE' GENERALE
browser.get(url_sg)
browser.find_element_by_xpath(xpath_sg).click() #Esportiamo in Excel 
time.sleep(2) #dorme 2 sec

#BNP PARIBAS
browser.get(url_bnp)
time.sleep(5)
browser.find_element_by_xpath(xpath_bnp0).click()
time.sleep(5)
browser.find_element_by_xpath(xpath_bnp1).click()
time.sleep(5)
browser.find_element_by_xpath(xpath_bnp2).click()

#COMMERZBANK
#andiamo sul sito di CommerzBank al fine di ritirare il file necessario .xls
browser.get(url_cb)
time.sleep(5)
browser.find_element_by_xpath(xpath_cb).click()

#BANCA IMI  
#ce un problema, occorre selezionare prima tutto - checkbox
browser.get(url_imi)
time.sleep(5)
browser.find_element_by_xpath(xpath_imi0).click()
time.sleep(5)
browser.find_element_by_xpath(xpath_imi1).click() #problema salvataggio automatico

#DEUTSCHE BANK
browser.get(url_db)
time.sleep(5)
browser.find_element_by_xpath(xpath_db0).click()
time.sleep(5)
browser.find_element_by_xpath(xpath_db1).click()
time.sleep(5)
browser.find_element_by_xpath(xpath_db2).click() 

#UNICREDIT GROUP
browser.get(url_ucg)
time.sleep(5)
browser.find_element_by_xpath(xpath_ucg0).click()
time.sleep(5)
browser.find_element_by_xpath(xpath_ucg1).click()


browser.close() # ciao browser
time.sleep(10)

os.chdir("\home\rlv\Desktop\As") #cambiare la directory desiderata
nomi = ["x1.xls","x2.xls", "x3.xls", "x4.xls", "x5.xls", "x6.xls"] #lista dei nomi
lista = os.listdir(".")
for i in lista:
    os.rename(i,nomi[lista.index(i)]) #modifichiamo i nomi dei file

# fp.set_preference('browser.download.dir', os.getcwd())

# ADESSO WEB-"SCRAPIAMO"  :) 

#filez = open(r'C:\Users\Rostyslav Lytvyn\Desktop\SG\PYTHON\output\output_sg.txt', 'w') # allochiamo un file per l'output csv
#url_alt = "http://www.aletticertificate.it/prodotti-e-prezzi/bonus/prezzi/" #URL della Banca Aletti
#xpath_alt0 = '/html/body/div[1]/div[2]/div[2]/div[4]/div/div[1]/div/div[1]/label/select'
#xpath_alt1 = '/html/body/div[1]/div[2]/div[2]/div[4]/div/div[1]/div/div[1]/label/select/option[4]'

#browser.get(url_alt)
#browser.find_element_by_xpath(xpath_alt0).click()
#browser.find_element_by_xpath(xpath_alt1).click() #adesso avremo 100 dati visualizzati per pagina


#r= requests.get(url_alt)
#soup= BeautifulSoup(r.content)

#alt_isin=soup.find_all("td", {"class": "sorting_1"})


#sg_dataName = soup.find_all("td", {"class": "underlyingName"},limit=16)
#sg_dataMat = soup.find_all("td", {"class": "maturity"},limit=16)
#sg_dataBonus = soup.find_all("td", {"class": "bonus"},limit=16)
#sg_dataCap = soup.find_all("td", {"class": "cap"},limit=16)
#sg_dataBarrier = soup.find_all("td", {"class": "barrier"},limit=16)
#sg_dataBarrPerc = soup.find_all("td", {"class": "barrierPercent"},limit=16)
#sg_dataBid = soup.find_all("td", {"class": "bid"},limit=16)
#sg_dataAsk = soup.find_all("td", {"class": "ask"},limit=16)
#sg_dataVar= soup.find_all("td", {"class": "var"},limit=16)
#sg_dataIsin = soup.find_all("td", {"class": "isin"},limit=16)
#sg_dataSymb = soup.find_all("td", {"class": "symbol"},limit=16)

#for item in sg_dataName:
 #   name= item.text
  #  filez.write(name)
#for item in sg_dataMat:
 #   mat= item.text
  #  filez.write(mat)
#for item in sg_dataBonus:
 #   bonus= item.text
  #  filez.write(bonus)
#for item in sg_dataCap:
 #   cap= item.text
  #  cap_enc= cap.encode('utf-8')
  #  filez.write(cap_enc)
#for item in sg_dataBarrier:
 #   barrier = item.text
  #  barrier_enc= barrier.encode('utf-8')
   # filez.write(barrier_enc)
#for item in sg_dataBarrPerc:
 #   barrPerc= item.text
  #  filez.write(barrPerc)
#for item in sg_dataBid:
 #   bid= item.text
  #  bid_enc= bid.encode('utf-8')
   # filez.write(bid_enc)
#for item in sg_dataAsk:
 #   ask = item.text
  #  ask_enc= ask.encode('utf-8')
   # filez.write(ask_enc)
#for item in sg_dataVar:
 #   var= item.text
  #  filez.write(var)
#for item in sg_dataIsin:
 #   isin= item.text
  #  filez.write(isin)
#for item in sg_dataSymb:
 #   symb= item.text
  #  filez.write(symb)

#print(url)
#print(name, mat, bonus, cap, barrier, barrPerc, bid, ask, var, isin,symb)
#filez.write(str(name) + str(mat) + str(bonus)+ '\n')

#filez.close



#-------------- CERTX ------------------

url_certx1='http://www.eurotlx.com/en/strumenti/ricerca-avanzata?redirect=1&category=CERT_X&subcategory=CERTIFICATES_NOT_EQUITY_PROTECTION'
url_certx2='http://www.eurotlx.com/en/strumenti/ricerca-avanzata?redirect=1&category=CERT_X&subcategory=CERTIFICATES_EQUITY_PROTECTION'
url_certx3='http://www.eurotlx.com/en/strumenti/ricerca-avanzata?redirect=1&category=CERT_X&subcategory=CERTIFICATES_PARTIAL_EQUITY_PROTECTION'
url_certx4='http://www.eurotlx.com/en/strumenti/ricerca-avanzata?redirect=1&category=CERT_X&subcategory=CERTIFICATES_LEVA'
url_certx5='http://www.eurotlx.com/en/strumenti/ricerca-avanzata?redirect=1&category=CERT_X&subcategory=COVERED_WARRANT'


xpath_certx1='/html/body/div[2]/div/div[1]/div[2]/div/div/div/form/div/div[2]/div[2]/div/a'
browser.get(url_certx1)
browser.find_element_by_xpath(xpath_certx1).click()

