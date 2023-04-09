import scrapy

from ..items import ReportItem


class ReportSpider(scrapy.Spider):
    page_number = 2
    name = 'reports'
    start_urls = [
        'https://president.az/az/news/category/all/1'
    ]

    def parse(self, response):
        global link
        link = response.css('article a::attr(href)').extract()


        for i in range(len(link)):
            yield response.follow(f'https://president.az{link[i]}', callback = self.parse_link)

        next_page = f'https://president.az/az/news/category/all/{ReportSpider.page_number}/'

        if ReportSpider.page_number < 779:
            ReportSpider.page_number += 1
            yield response.follow(next_page, callback =self.parse)







    def parse_link(self, response):
        items = ReportItem()
        title = response.css('.news_heading::text').extract()
        items['title'] = title
        category = response.css('.breadcrumbs_item:nth-child(1) .breadcrumbs_link::text').extract()
        items['category'] = category
        subcategory = response.css('.active-link-events::text').extract()
        items['subcategory'] = subcategory
        datetime = response.css('.news_date::text').extract()
        items['datetime'] = datetime

        for i in range(len(link)):
            items['link'] = f'https://president.az{link[i]}'
        image = response.css('.news_image img::attr(src)').extract()
        items['image'] = image
        content = response.css('.news_paragraph-block p::text').extract()
        items['content'] = content


        yield items

