import requests
import json
from bs4 import BeautifulSoup

#https://www.youtube.com/watch?v=nCuPv3tf2Hg&list=PLRzwgpycm-Fi5Pe_W2HwEwyvcB5-SJLB7&index=8

baseurl = 'https://www.thewhiskyexchange.com/'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

r = requests.get('https://www.thewhiskyexchange.com/c/35/japanese-whisky')
soup = BeautifulSoup(r.content, 'lxml')

productlist = soup.find_all('li', class_ = 'product-grid__item')

print(productlist)

productlinks = []

for item in productlist:
    for link in item.find_all('a', href=True):
        print(link['href'])

    
