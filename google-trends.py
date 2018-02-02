from pytrends.request import TrendReq
import pandas as pd
import importlib


keyword = 'Bitcoin'

pytrend = TrendReq(hl='de-CH', geo='CH')

# Get Google Hot Trends data
trending_searches_df = pytrend.trending_searches()
# trending_searches_df.sort_values(by='trafficBucketLowerBound', ascending=False, inplace=True)
print(trending_searches_df)

pytrend.build_payload(kw_list=[keyword], timeframe='today 1-m', geo='CH', gprop='news')

# Interest Over Time
interest_over_time_df = pytrend.interest_over_time()
print(interest_over_time_df.head())

# Interest by Region
interest_by_region_df = pytrend.interest_by_region().reset_index()
print(interest_by_region_df.head())

# Google suggestions
suggestions_dict = pytrend.suggestions(keyword=keyword)
print('suggestions_dict:\n{}'.format(suggestions_dict))

# related topics
related_topics_df = pytrend.related_topics()[keyword]
print(related_topics_df.head())