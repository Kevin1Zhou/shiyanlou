# -*- coding=utf-8 -*-

import scrapy

Class ShiyanlouGithubSpider(scrapy.Spider):
	name = 'shiyanlou-github'
	
	@property
	def start_urls(self):
		url_temp = 'https://github.com/shiyanlou?page={}&tab=repositories'
		urls = (url_temp.format(i) for i in range(1,5))
		return urls
	def parse(self,response):
		for base in response.css('li.col-12'):
			yield {
				'name': base.xpath('.//a[@itemprop="name codeRepository"]/text()').re('\n\s*(.*)'),
				'update_time': base.xpath('.//relative-time/@datetime').extract()
				}
	