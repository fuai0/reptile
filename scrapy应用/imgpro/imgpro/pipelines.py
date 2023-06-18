# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

#
# class ImgproPipeline:
#     def process_item(self, item, spider):
#         return item

from scrapy.pipelines.images import ImagesPipeline
import scrapy
class imgproPipeline(ImagesPipeline):

    # 根据图片的地址返回图片数据
    def get_media_requests(self, item, info):
        yield scrapy.Request(item["src"])

    # 染回图片名称
    def file_path(self, request, response=None, info=None, *, item=None):
        imgname = request.url.split('/')[-1]
        return imgname

    # 返回下一个被执行的管道类
    def item_completed(self, results, item, info):
        return item
