from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor
from scrapy.item import Item, Field

class CustomItem(Item):
    title = Field()
    contents = Field()

class NotesSpider(CrawlSpider):
    name = 'notes'
    allowed_domains = ['deepmind.com']
    start_urls = ['https://www.deepmind.com/blog']
    rules = (
        Rule(LinkExtractor(allow='page=')),
        Rule(LinkExtractor(), callback='parse_item'),
    )

    def parse_item(self, response):
        note_contents = ''
        for p in response.xpath('//p//text()').getall():
            note_contents += p + '\n'

        item = CustomItem()
        item['title'] = response.xpath('//title//text()').get()
        item['contents'] = note_contents

        return item

