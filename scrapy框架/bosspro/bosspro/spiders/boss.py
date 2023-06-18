import scrapy


class BossSpider(scrapy.Spider):
    name = 'boss'
    # allowed_domains = ['www.xxx.com']
    start_urls = []
    for i in range(10):
        start_urls.append(f"https://www.zhipin.com/web/geek/job?query=Python&city=101110100&page={i+1}")
    print(start_urls)

    def parse_detail(self,response):
        pass


    def parse(self, response):
        li_list = response.xpath('/html/body/div[1]/div[2]/div[2]/div/div[1]/div[2]/ul/li')
        print(li_list)
        for li in li_list:
            name = li.xpath('//div[@class="job-title"]/span[1]/text()').extract_first()
            print(name)
            # 请求传参
            yield scrapy.Request(url=url_detail,callback=self.parse_detail,meta={"item":item})

