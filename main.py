FORMULQR_URL = "https://forms.gle/gNSEL1FM2qUDWpP66"
from webscraping import ZillowScrap
from pprint import pprint
data = ZillowScrap()
links = data.list_of_links()
adresses = data.list_of_adresses()
prices = data.list_of_prices()
pprint(links)
print(adresses)
print(prices)