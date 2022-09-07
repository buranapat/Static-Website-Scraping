import requests
from bs4 import BeautifulSoup

#create list of sector
sectors = ['AGRI','FOOD','FASHION','HOME','PERSON','BANK','FIN','INSUR','AUTO','IMM','PAPER'
          ,'PETRO','PKG','STEEL','CONMAT','PROP','PF%26REIT'
          ,'CONS','ENERG','MINE','COMM','HELTH','MEDIA','PROF','TOURISM','TRANS','ETRON','ICT']

#create dictionary to store list of stock's name
stock_in_sector = {}

#input sector's abbreviation
sector = input("which sector (Ex. ICT, FASHION) :").upper()

#have to covert PF&REIT to PF%26REIT to find website
if sector == 'PF&REIT' :
    sector = 'PF%26REIT'
elif sector not in sectors:
    print("don't have this sector, please try again")
    
#scrape stock's name
url = f"https://classic.set.or.th/mkt/sectorquotation.do?market=SET&sector={sector}&language=th&country=TH"
source = requests.get(url).text
stock_name = []
soup = BeautifulSoup(source,'lxml')
stocks = soup.find(
            'div',
            id ='maincontent' ).find( 
            'div',
            class_ = 'row').findChildren(
            'div',
            class_ = 'row',
            recursive = False)[1].findChildren(
            'tbody',
            recursive = True)[1].findChildren(
            'tr')
# store each stock name into list named stock_name
for i in range(len(stocks)):
    stock_name += [stocks[i].text.replace("\n","").replace("\r","").strip().split()[0]]

# convert PF%26REIT back to PF&REIT to make it easier to read
if sector == 'PF%26REIT' :
    sector = 'PF&REIT'
    
# store stock_name into dictionary named stock_in_sector
stock_in_sector[sector] = stock_name

print(stock_in_sector)