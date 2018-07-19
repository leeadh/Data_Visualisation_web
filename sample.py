from bs4 import BeautifulSoup
import urllib2
import requests

url = "https://www.cartrade.com/buy-used-cars"
i=2
next_url = "https://www.cartrade.com/buy-used-cars/p-" + str(i)
page = urllib2.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
values = soup.find_all('div', attrs={'class': 'btmMrg carlistblk'})
for item in values:
	URL = item.find(itemprop="image").get('content')
	title = item.find('div',attrs={'class':'carimgblk'}).img['title']
	price = item.find('div',attrs={'class':'cr_prc'}).text
	print(URL)

while True:
	i=i+1
	page = requests.get(next_url)
	if page.status_code != 200:
		break
	next_url = "https://www.cartrade.com/buy-used-cars/p-" + str(i)
	values = soup.find_all('div', attrs={'class': 'btmMrg carlistblk'})
	for item in values:
		URL = item.find(itemprop="image").get('content')
		title = item.find('div',attrs={'class':'carimgblk'}).img['title']
		price = item.find('div',attrs={'class':'cr_prc'}).text
		print("----------")
		print(i)
		print(URL)
		print(title)
		print(price)
		print("----------")