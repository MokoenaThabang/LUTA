from itertools import product
from xml.dom.minidom import Attr
from bs4 import BeautifulSoup
import ssl
import certifi
import requests
from fastapi import FastAPI
import urllib3



app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello Welcome to the LUTA API"}


@app.get("/getProduct/{id}")
def getProducts(id):
    
    
    url1='https://www.shoprite.co.za/search/all?q={0}'.format(id)
    url2='https://www.makro.co.za/search/?text={0}'.format(id)
    url3='https://www.pnp.co.za/pnpstorefront/pnp/en/search/?text={0}'.format(id)
    

   
    products=[]
    products.append(Scrape_Shoprite(url1)) 
    products.append(Scrape_Makro(url2))
    products.append(Scrape_Pnp(url3))

    return products
    
   
    
    


def Scrape_Shoprite(url:str):
    html_req=requests.get(url).text
    soup= BeautifulSoup(html_req,'lxml')
    products=soup.find('figcaption',class_='item-product__caption')
    soup2=BeautifulSoup(html_req,'html.parser')
    product_name=products.find('h3',class_='item-product__name').text
    product_price=products.find('span',class_="now").text
    image=soup2.find_all('img',src=True)
    it=[]
    for item in image:
        it=item['src']
        
    er={ 'Product Name ':{product_name},
      'Product_Price':{product_price},
      'Product img' :{it}
     }
    return er 
  
      
      





def Scrape_Pnp(url:str):
    html_req2= requests.get(url).text
    soup2=BeautifulSoup(html_req2,'lxml')
    soup=BeautifulSoup(html_req2,'html.parser')
    product2=soup2.find('div',class_='item')
    
    product_price2=product2.find('div',class_='currentPrice').text.replace('\r','').replace('\n','').replace('\t','')
    product_name2=product2.find('div',class_='item-name').text
    image=soup.find_all('img',src=True)
    it=[]
    for item in image:
        it=item['src']
    
     
    er={ 'Product Name ':{product_name2},
      'Product_Price':{product_price2},
      'Product img' :{it}
     }
    return er 
    


def Scrape_Makro(url:str):
    html_req2= requests.get(url).text
    soup2=BeautifulSoup(html_req2,'lxml')
    soup=BeautifulSoup(html_req2,'html.parser')
    product2=soup2.find('div',class_='product-tile-inner')
    product_price2=product2.find('p',class_='price').text
    product_name2=product2.find('a',class_='product-tile-inner__productTitle').text
    image=soup.find_all('img',src=True)
    it=[]
    for item in image:
        it=item['src']
        
    er={ 'Product Name ':{product_name2},
      'Product_Price':{product_price2},
      'Product img' :{it}
     }
    return er
    

















