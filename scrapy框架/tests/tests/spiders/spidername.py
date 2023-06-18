import scrapy
from tests.items import TestsItem

class SpidernameSpider(scrapy.Spider):
    # 爬虫文件名称：爬虫源文件唯一标识
    # name = 'spidername'
    # # # 允许的域名：限定了表里的哪些url会被请求发送
    # # allowed_domains = ['www.xxx.com']
    # # 起始的url列表：该列表里的url会被scrapy自动请求发送
    # start_urls = ['https://www.xiaohua.com/duanzi/']
    #
    # # 数据解析：response是请求成功后的响应数据
    # def parse(self, response):
    #     div_list = response.xpath("//div[@class='content-left']/div")
    #     list = []
    #     for div in div_list:
    #         # xpath返回的是列表，但列表元素一定是Selector元素
    #         # extract可以将selector的data参数存储字符串参数提取出来
    #         anthor = div.xpath("./div/div/a/i/text()").extract()
    #         anthor = "".join(anthor)
    #         duanzi = div.xpath("./p/a/text()").extract()
    #         duanzi = "".join(duanzi)
    #
    #         dic = {"anthor":anthor,"duanzi":duanzi}
    #         list.append(dic)
    #     return list


    name = 'spidername'

    start_urls = ['https://www.xiaohua.com/duanzi/']

    def parse(self, response):
        div_list = response.xpath("//div[@class='content-left']/div")

        for div in div_list:
            anthor = div.xpath("./div/div/a/i/text()").extract()
            anthor = "".join(anthor)
            duanzi = div.xpath("./p/a/text()").extract()
            duanzi = "".join(duanzi)

            # 把解析的数据封装到item当中
            item = TestsItem()
            item["anthor"] = anthor
            item["content"] = duanzi

            # 把item提交给管道
            yield item