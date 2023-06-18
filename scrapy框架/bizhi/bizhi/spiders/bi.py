import requests
import scrapy
from bizhi.items import BizhiItem

class BiSpider(scrapy.Spider):
    name = 'bi'
    # allowed_domains = ['www.xxx.com']
    # https://pic.netbian.com/pingban/index_2.html
    start_urls = []
    start_urls.append("https://pic.netbian.com/pingban/")
    for i in range(18):
        start_urls.append(f"https://pic.netbian.com/pingban/index_{i+2}.html")

    def parse(self, response):
        li_list = response.xpath('//ul[@class="clearfix"]/li')

        for li in li_list:
            url_img = li.xpath('./a/img/@src').extract_first()
            img_name = li.xpath('./a/img/@alt').extract_first()
            url_list = "https://pic.netbian.com" + url_img
            img_data = requests.get(url_list).content

            item = BizhiItem()
            item["name"] = img_name
            item["data"] = img_data
            yield item

