import requests
import json
from bs4 import BeautifulSoup

#https://www.youtube.com/watch?v=nCuPv3tf2Hg&list=PLRzwgpycm-Fi5Pe_W2HwEwyvcB5-SJLB7&index=8

baseurl = 'https://www.alibaba.com/product-detail/Looks-more-elegant-jelly-adhesives-stick_1600651641747.html'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36'
}

r = requests.get('https://www.alibaba.com/product-detail/Looks-more-elegant-jelly-adhesives-stick_1600651641747.html')
soup = BeautifulSoup(r.content, 'lxml')

productlist = soup.find_all('div', class_='sku-option')

title = soup.find('h1').text.strip()
price = soup.find('span', class_='promotion').text.strip()

# print(price)

productlinks = []

for item in productlist:
    for link in item.find_all('img', src=True):
        productlinks.append(link['src'])

output = {
    'title': title,
    'price': price,
    'variant_image': productlinks
}
# print(title,price,productlinks)
print(output)