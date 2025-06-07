# Importing libraries
from bs4 import BeautifulSoup as BS
import requests

# Method to get the price of gold
def get_price(url):
    # Getting the request from url 
    data = requests.get(url)

    # Converting the text 
    soup = BS(data.text, 'html.parser')

    # Finding the correct element containing the price
    ans = soup.find("div", class_="BNeawe iBp4i AP7Wnd")

    # Returning the price text
    return ans.text if ans else "Price not found"

# URL of the gold price
url = "https://goldprice.org/gold-price-india.html"

# Calling the get_price method
ans = get_price(url)

# Printing the ans
print(ans)
