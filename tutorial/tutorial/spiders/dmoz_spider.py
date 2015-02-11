__author__ = 'keshav'
import scrapy
import urlparse

from tutorial.items import DmozItem
from tutorial.items import ColorItem


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
                yield scrapy.Request("http://www.flipkart.com" + link)

        else:
            major_path = response.xpath('//div[@class="product-details line"]')
            item = DmozItem()
            item['title'] = major_path.xpath('div[1]/h1/text()').extract()
            item['category'] = major_path.xpath('div[1]/@data-pagename').extract()
            item['price'] = major_path.xpath('//span[@class="selling-price omniture-field"]/text()').extract()
            shirts = []
            default = ColorItem()
            default['color'] = major_path.xpath(
                'div[@class="multiSelectionWrapper section line"]/div[1]/div[2]/div/@title').extract()
            default['im_link'] = major_path.xpath(
                'div[@class="multiSelectionWrapper section line"]/div[1]/div[2]/div/div/@data-image').extract()
            shirts.append(default)

            for myp in major_path.xpath('//a[@class="multiSelectionWidget-selector-link"]'):
                color = ColorItem()
                shirt_link = myp.xpath('div/div/@data-image').extract()
                shirt_link = ''.join(shirt_link).strip()
                if shirt_link != '':
                    color['color'] = myp.xpath('div/div/span/text()').extract()
                    color['im_link'] = shirt_link
                shirts.append(color)
            item['shirts'] = shirts
            yield item
