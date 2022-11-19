import scrapy
from lianjiaspider.items import NewhouseItem


class newhouseSpider(scrapy.spiders.Spider):
    name = "newhouse"   #爬虫名：newhouse
    allowed_domains = ["bj.fang.lianjia.com"]
    start_urls = ["https://bj.fang.lianjia.com/loupan/pg3/"]
    custom_setting = {
        'ITEM_PIPELINES':{'lianjiaspider.piplines.NewhousePipeline':300},
    }

    def start_requests(self):
        for i in range(3, 8):
            yield scrapy.Request("https://bj.fang.lianjia.com/loupan/pg{}/".format(i),callback=self.parse)

    def parse(self,response):
        item = NewhouseItem()
        for each in response.xpath("/html/body/div[3]/ul[2]/li[*]"):
            item["loupan"]=each.xpath("./div/div[1]/a/text()").extract_first()
            item["types"] =each.xpath("./div/div[1]/span[1]/text()").extract_first()
            item["location"]=each.xpath("./div/div[2]/a/text()").extract()
            item["rooms"] = each.xpath("./div/a/span/text()").extract()
            item["price_per_m2"] = each.xpath("./div/div[6]/div[1]/span[1]/text()").extract()
            item["price_all"] = each.xpath("./div/div[6]/div[2]/text()").extract()
            item["area"] = each.xpath("./div/div[3]/span/text()").extract()
            yield item

