from scrapy import cmdline
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from twisted.internet import reactor

from lianjiaspider.spiders.spider import newhouseSpider
from lianjiaspider.spiders.spider2 import oldhouseSpider

#configure_logging()
runner = CrawlerRunner()
runner.crawl(newhouseSpider)
runner.crawl(oldhouseSpider)
d = runner.join()
d.addBoth(lambda _:reactor.stop())

reactor.run()
