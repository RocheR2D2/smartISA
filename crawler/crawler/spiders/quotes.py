# -*- coding: utf-8 -*-
import scrapy


class QuotesSpider(Spider):
    name = "titles"
    allowed_domains = ["investmentpolicyhub.unctad.org"]

    def parse(self, response):
  
        short_title = response.xpath('//*[@id="case-short-title"]/text()').extract_first()
        full_title = response.xpath('//*[@id="case-full-title"]/text()').extract_first()
        arbitrail_rules = response.xpath('//*[@id="rules-institution-content"]/div[1]/div/text()').extract_first()
        decisions_rendered = response.xpath('//*[@id="decisions-content"]//div[last()]/a/text()').extract_first()

        yield{
        	'short_title': short_title,
        	'full_title': full_title,
        	'arbitrail_rules': arbitrail_rules,
        	'decisions_rendered': decisions_rendered}

