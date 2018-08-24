'''
Do a little scraping or API-calling of your own. Formally, your goal is to write a scraper that will:

1) Return specific pieces of information (rather than just downloading a whole page)
2) Iterate over multiple pages/queries
3) Save the data to your computer

Once you have your data, compute some statistical summaries and/or visualizations
that give yousome new insights into your scraping topic of interest.
'''
import scrapy
from scrapy.crawler import CrawlerProcess

class WebSpider(scrapy.Spider):
	name = 'pullprices'
	start_urls = ['http://www.businessinsider.com']

	def parse(self, response):
		titles = response.xpath("//div[class='river']/div/h2/a[class='title']/text()").extract()
		pages = response.xpath("//div[class='river']/div/h2/a[class='title']/attr(href)")

		for item in zip(titles, pages):
			scraped_info = {
				'title': item[0],
				'page': item[1]
			}

		yield scraped_info

process = CrawlerProcess({
	'FEED_FORMAT': 'json',
	'FEED_URI': '2 data.json',
	'LOG_ENABLED': False,
	'ROBOTSTXT_OBEY': True,
	'USER_AGENT': 'ThinkfulDataScienceBootcampCrawler (thinkful.com)',
	'AUTOTHROTTLE_ENABLED': True,
	'HTTPCACHE_ENABLED': True
})
process.crawl(WebSpider)
process.start()

import pandas as pd
webpage = pd.read_json('2 file.json', orient='records')

print(webpage.shape)
print(webpage.head())
