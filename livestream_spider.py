import scrapy
from config import Config

class LiveStreamSpider(scrapy.Spider):
    name = "livestream_spider"
    start_urls = [Config.STREAM_URL]  # Replace with the actual URL

    def parse(self, response):
        # Use custom CSS selectors to identify live streams
        for stream in response.css(Config.HTML_ELEMENT):
            yield {
                'title': stream.css('h2::text').get(),
                'url': stream.css('a::attr(href)').get(),
            }
