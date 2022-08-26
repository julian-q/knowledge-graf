import scrapy

class NotesSpider(scrapy.Spider):
    name = 'notes'
    start_urls = ['https://www.lindaktong.com/bookshelf/ride-of-a-lifetime']

    def parse(self, response):
        note_contents = ''
        for p in response.xpath('//div[@data-layout-label="Post Body"]//p//text()').getall():
            note_contents += p + '\n'
        yield {
            'title': response.xpath('//h1[@data-content-field="title"]//text()').get(),
            'contents': note_contents
        }

        next_page = response.xpath('//a[@class="item-pagination-link item-pagination-link--next"]/@href').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
