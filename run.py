from bs4 import BeautifulSoup
import json
import requests, re, datetime

def itemScan(link):
	page = requests.get(link)
	soup = BeautifulSoup(page.content, 'html.parser')
	results = soup.find('div', class_='product-row card-mobile card-tablet')

	priceMain = results.find('div',  id='product_price_brutto')
	price = re.findall(r'\b\d+\b', list(str(priceMain).split(" "))[2])
	priceOutPut = int(price[0])
	if len(price) == 2:
		price = re.findall(r'\d+\.\d+', list(str(priceMain).split(" "))[2])
		priceOutPut = float(price[0])

	stocks = results.find('div', class_='prod-available-items')
	stocks = re.findall(r'\b\d+\b', str(stocks))


	results_id = soup.find('div', class_='product-specification__group')
	rows = results_id.find_all('div', class_='specification__row')
	product_ID = re.findall(r'\b\d+\b', str(rows[2].find('span', class_='specification__value')))
	return priceOutPut, int(stocks[0]), product_ID[0]



link = 'https://www.morele.net/gamepad-pdp-arctic-white-049-012-eu-wh-9355965/'


price, sztuki, ID = itemScan(link)

print(price, sztuki, ID)

