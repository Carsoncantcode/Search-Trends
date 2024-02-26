from pytrends.request import TrendReq
import matplotlib.pyplot as plt

def trending_searches(keywords):
    pytrends = TrendReq(hl='en-US', tz=480)

    pytrends.build_payload(keywords, cat=0, timeframe='now 4-H', geo='US', gprop='')

    search_data = pytrends.interest_over_time()

    return search_data

search_terms = ["Blockchain", "Bitcoin", "ETH", "Crypto", "Binance"]

data = trending_searches(search_terms)

print(data)

plt.figure(figsize=(20, 12))
ax = plt.gca()
data.plot(ax=ax, title='Google Trends')
plt.xlabel('Date')
plt.ylabel('Interest')
plt.show()