# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json

class NewhousePipeline(object):
    def open_spider(self,spider):
        try:
            self.file=open('scrapy-test-lianjia-newhouse.json',"w",encoding="utf-8")
        except Exception as err:
            print(err)


    def process_item(self, item, spider):
        dict_item =dict(item)
        json_str =json.dumps(dict_item,ensure_ascii=False)+"\n"
        self.file.write(json_str)
        return item

    def close_spider(self,spider):
        self.file.close()

class OldhousePipeline(object):
    def open_spider(self,spider2):
        try:
            self.file=open('scrapy-test-lianjia-oldhouse.json',"w",encoding="utf-8")
        except Exception as err:
            print(err)


    def process_item(self, item, spider2):
        dict_item =dict(item)
        json_str =json.dumps(dict_item,ensure_ascii=False)+"\n"
        self.file.write(json_str)
        return item

    def close_spider(self,spider2):
        self.file.close()