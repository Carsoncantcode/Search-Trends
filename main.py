from pytrends.request import TrendReq
import matplotlib.pyplot as plt

def trending_searches(keywords, timeframe):
    pytrends = TrendReq(hl='en-US', tz=480)
    pytrends.build_payload(keywords, cat=0, timeframe=timeframe, geo='US', gprop='')
    search_data = pytrends.interest_over_time()
    return search_data

search_terms = ["Blockchain", "Bitcoin", "ETH", "Crypto", "Binance"]
timeframes = ['now 4-H', 'now 1-H', 'today 3-m', 'all']

fig, axs = plt.subplots(2, 2, figsize=(20, 12))

axs = axs.flatten()

for ax, timeframe in zip(axs, timeframes):
    data = trending_searches(search_terms, timeframe)
    data.plot(ax=ax, title=f'Trends: {timeframe}')
    ax.set_xlabel('Date')
    ax.set_ylabel('Interest')
    ax.legend(search_terms)

plt.tight_layout()  
plt.savefig('google_trends_plot_combined.png', dpi=300)
plt.show()
