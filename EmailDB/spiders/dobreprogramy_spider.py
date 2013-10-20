__author__ = 'jurek'
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from EmailDB.items import EmaildbItem
import re


class dobreprogramy_Spider(CrawlSpider):
    database = {}
    name = "dobreprogramy_spider"
    allowed_domains = ["forum.dobreprogramy.pl"]
    start_urls = ["http://forum.dobreprogramy.pl/gielda-f45.html"]
    rules = (
        Rule(SgmlLinkExtractor(deny=(r'^post')), follow=True, callback='parse_item'),
    )

    r = re.compile(
        r"""
    # The username (capture it)
    (?P<username>\w+)
    # followed by @
    @
    # followed by the domain (also capture it)
    (?P<domain>(\w+\.)+\w+)""",
        re.VERBOSE | re.IGNORECASE)
    log_file = open('/home/jurek/logsy', 'w')


    def parse_item(self, response):
        try:
            hxs = HtmlXPathSelector(response)
            inners = hxs.select('//div[@class="inner"]')
            inners_with_posts = []

            for inner in inners: #Copy to inner_with_posts that div blocks which cointains posts.
                if len(inner.select('.//div[@class="content"]').extract()) > 0:
                    inners_with_posts.append(inner)

            for inner in inners_with_posts:
                usr = inner.select('.//a[@class="dp_username"]/text()').extract()
                post = inner.select('.//div[@class="content"]').extract()
                pre_email = self.r.findall(post[0].encode('utf-8'))

                if len(pre_email) > 0:
                    try:
                        email = pre_email[0][0] + '@' + pre_email[0][1]
                        url = response.url
                        usr = usr[0]
                        yield EmaildbItem(user=usr, url=url, email=email)
                    except IndexError:
                        print('Cannot get username')
        except AttributeError:
            print('...')
