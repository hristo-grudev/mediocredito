import re

import scrapy

from scrapy.loader import ItemLoader
from ..items import MediocreditoItem
from itemloaders.processors import TakeFirst


class MediocreditoSpider(scrapy.Spider):
	name = 'mediocredito'
	start_urls = ['https://www.mediocredito.it/Comunicazione/News']

	def parse(self, response):
		article_links = response.xpath('//h3/a/@href')
		yield from response.follow_all(article_links, self.parse_post)

		next_page = response.xpath('//ul[@class="pagination"]/li/a[span]')
		yield from response.follow_all(next_page, self.parse)

	def parse_post(self, response):
		title = response.xpath('//h1/text()').get()
		description = response.xpath('//div[@class="col-lg-8"]//text()[normalize-space()]').getall()
		description = [p.strip() for p in description]
		description = ' '.join(description).strip()
		date = response.xpath('//span[@class="entry-date"]/text()').get()
		if date:
			date = re.findall(r"(\d+\s[a-zA-Z]+\s\d+)", date)[0]

		item = ItemLoader(item=MediocreditoItem(), response=response)
		item.default_output_processor = TakeFirst()
		item.add_value('title', title)
		item.add_value('description', description)
		if date:
			item.add_value('date', date)

		return item.load_item()
