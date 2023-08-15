from bs4 import BeautifulSoup
import requests
import pandas as pd
url = "https://www.coingecko.com/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")
results = soup.find("div", {"class": "coingecko-table"}).find("tbody").find_all("tr")

# creating a empty list
names = []
price = []
volume_24h = []
market_cap = []

for result in results:

    try:
        names.append(result.find("span", {"class": "lg:tw-flex font-bold tw-items-center tw-justify-between"}).get_text().strip())
    except:
        names.append("n/a")
    try:
        price.append(result.find("td", {"class": "td-price price text-right"}).get_text().strip())
    except:
        price.append("n/a")
    try:
        volume_24h.append(result.find("td", {"class": "td-liquidity_score lit text-right col-market"}).get_text().strip())
    except:
        volume_24h.append("n/a")
    try:
        market_cap.append(result.find("td", {"class": "td-market_cap cap col-market cap-price text-right"}).get_text().strip())
    except:
        market_cap.append("n/a")

crypto_df = pd.DataFrame({"Coin": names, "Price": price,"24h_Volume": volume_24h, "Market_Cap": market_cap})
crypto_df.to_csv("crypto_df.csv", index=False)
