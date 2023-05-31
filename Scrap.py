import scrapy
import re

class MedspiderSpider(scrapy.Spider):
    name = "medspider"
    allowed_domains = ["www.1mg.com"]
    start_urls = ["https://www.1mg.com/drugs-all-medicines"]

    def parse(self, response):
        meds = response.css('div.style__flex-1___A_qoj'),
        element = response.css('li.next a ::attr(href)').get(),
        link = re.findall('href="(.*?)"', element)[0],
        print(link),
        for med in meds:
            yield{
                'name' : med.css('div div::text').get(),
                'price' : med.css('div:has(> span)::text').getall()[-1],
                'strip content' :  med.css('div::text').getall()[-4],
                'manufacturer' :  med.css('div::text').getall()[-3],
            }
       
