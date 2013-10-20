# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

class dobreprogramyPipeline(object):
    log_file = open('/home/jurek/spider_log', 'w')
    DB = set()
    def process_item(self, item, spider):
        return item
