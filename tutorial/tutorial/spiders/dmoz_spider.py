__author__ = 'keshav'
import scrapy
import urlparse

from tutorial.items import DmozItem


class DmozSpider(scrapy.Spider):
    name = "Flipkart"
    allowed_domains = ["flipkart.com"]
    start_urls = [
        "http://www.flipkart.com/search?sid=search.flipkart.com&q=t+shirt"

    ]

    def parse(self, response):
        if response.url == DmozSpider.start_urls[0]:
            for sel in response.xpath('//div[@class="pu-visual-section"]'):
                link = sel.xpath('a/@href').extract()
                link = ''.join(link).strip()
                parsed_url = urlparse.urlparse(link)
                # now add this url to iterate over
                yield scrapy.Request("http://www.flipkart.com"+link)

        else:
            item = DmozItem()
            item['title'] = response.xpath('//div[@class="product-details line"]/div[1]/h1/text()').extract()
            item['subtitle'] = response.xpath('//div[@class="product-details line"]/div[1]/span/text()').extract()
            item['category'] = response.xpath('//div[@class="product-details line"]/div[1]/@data-pagename').extract()
            item['review_link'] = response.xpath('//div[@class="reviews"]/a/@href').extract()
            item['price'] = response.xpath('//span[@class="selling-price omniture-field"]/text()').extract()
            yield item
