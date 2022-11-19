import scrapy
from lianjiaspider.items import OldhouseItem

class oldhouseSpider(scrapy.spiders.Spider):
    name = "oldhouse"
    allowed_domains = ["bj.lianjia.com"]
    start_urls = ["https://bj.lianjia.com/ershoufang/pg3/"]
    custom_setting = {
        'ITEM_PIPELINES': {'lianjiaspider.piplines.OldhousePipeline': 300},
    }

    def start_requests(self):
        for i in range(3, 8):
            yield scrapy.Request("https://bj.lianjia.com/ershoufang/pg{}/".format(i),callback=self.parse)

    def parse(self,response):
        item = OldhouseItem()
        for each in response.xpath("/html/body/div[4]/div[1]/ul/li[*]"):
            item["estate"]=each.xpath("./div[1]/div[2]/div/a/text()").extract()
            item["price_per_m2"] = each.xpath("./div[1]/div[6]/div[2]/span/text()").extract()
            item["price_all"] = each.xpath("./div[1]/div[6]/div[1]/span/text()").extract()
            item["info"]=each.xpath("./div[1]/div[3]/div/text()").extract()
            yield item
