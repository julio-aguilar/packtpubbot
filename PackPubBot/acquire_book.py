from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = 'https://www.packtpub.com/packt/offers/free-learning'
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
title = soup('h2')
print(title)
#description = soup.find('div',{"id":"deal-of-the-day"})[7].get_text #'div',{'class': 'dotd-title'})
#description = soup.find_all('div')
#print(description)
# for line in description:
#     print(line)
book_text = ''.join(title[0].contents)
book = "<https://www.packtpub.com/packt/offers/free-learning|" + ''.join(title[0].contents)+ ">"
print(book_text)
image_url_list = soup('img')
mydivs = soup.findAll("div", {"class": "product_img"})
free_book_image_url = image_url_list[1]['src'].replace(' ', '%20')
print(mydivs)
print(free_book_image_url)