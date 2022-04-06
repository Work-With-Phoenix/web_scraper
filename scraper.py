import requests

from bs4 import BeautifulSoup, BeautifulStoneSoup

import pandas as pd

import json

baseurl = 'https://www.jumia.co.ke/'

headers = {
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
}

productlinks = [] 
  
for x in range (1,3):
    d = requests.get(f'https://www.jumia.co.ke/tcl/?q=tcl+smart+android+tv&page={x}#catalog-listing')
    soup = BeautifulSoup(d.content, 'lxml')

    cataloglist = soup.find_all('article', class_='prd')
    for prd in cataloglist:
        for link in prd.find_all('a', href=True):
            productlinks.append(baseurl + link['href'])


productlist = []
for link in productlinks:
    d = requests.get(link, headers=headers)
    soup = BeautifulSoup(d.content, 'lxml')

    name = soup.find('h1', class_='-pts').text.strip()
    rating = soup.find('div', class_='stars').text.strip()
    reviews = soup.find('a', class_='-plxs _more').text.strip()
    currentprice = soup.find('span', class_="-b").text.strip()
    # originalprice = soup.find('span', class_='-tal -gy5 -lthr -fs16').text.strip()
    # discount = soup.find('span', class_='tag _dsct _dyn -mls').text.strip()
    features = soup.find('article', class_='-pvs').text.strip()


    product = {
        'name':name,
        'rating':rating,
        'reviews':reviews,
        'currentprice':currentprice,
        # 'discount':discount,
        # 'originalprice':originalprice,
        'features':features
    }

    productlist.append(product)
    print('Saving', product)

df = pd.DataFrame(productlist, columns=['name', 'rating', 'reviews','originalprice', 'discount', 'currentprice', 'features' ])
print(df)

df.to_json(r'data/tvs.json', orient='records')