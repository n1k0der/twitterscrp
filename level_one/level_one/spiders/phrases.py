from gc import callbacks

import scrapy


class PhrasesSpider(scrapy.Spider):
    name = "phrases"
    allowed_domains = ["quotes.toscrape.com"]
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        quotes = response.css('.quote')
        print('*************************')

        for quote in quotes:
            saved_quote = {
                'author': quote.css('span .author::text').get(),
                'quote': quote.css('.text ::text').get(),
            }
            print('*************************')
            print(saved_quote)
            yield saved_quote

        next_page = response.css('.next a').xpath('@href').extract()[0]

        if next_page is not None:
            next_page_url = "https://quotes.toscrape.com" + next_page
            yield response.follow(next_page_url, callback = self.parse)