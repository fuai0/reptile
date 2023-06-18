import scrapy
from imgpro.items import ImgproItem


class ImgSpider(scrapy.Spider):
    name = 'img'
    # allowed_domains = ['www.xxx.com']
    start_urls = []
    # https://sc.chinaz.com/tupian/gudianmeinvtupian_2.html''
    start_urls.append("https://sc.chinaz.com/tupian/gudianmeinvtupian.html")
    for i in range(6):
        start_urls.append(f"https://sc.chinaz.com/tupian/gudianmeinvtupian_{i+2}.html")

    def parse(self, response):
        div_list = response.xpath('/html/body/div[3]/div[2]/div')
        for div in div_list:
            name = div.xpath('./img/@alt').extract_first()
            src = "https:"+div.xpath('./img/@data-original').extract_first()

            item = ImgproItem()

            item["src"] = src

            yield item

