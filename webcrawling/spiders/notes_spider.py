from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.item import Item, Field

class CustomItem(Item):
    title = Field()
    contents = Field()
    url = Field()

class NotesSpider(CrawlSpider):
    name = 'notes'
    rules = (
            Rule(LinkExtractor(allow='page=')),
            Rule(LinkExtractor(), callback='parse_item'),
        )
    allowed_domains = ['acquired.fm']
    start_urls = ['https://acquired.fm/episodes']

    def parse_item(self, response):
        note_contents = ''
        for p in response.xpath('//p//text()').getall():
            note_contents += p + '\n'

        item = CustomItem()
        item['title'] = response.xpath('//title//text()').get()
        item['contents'] = note_contents
        item['url'] = response.url

        return item

