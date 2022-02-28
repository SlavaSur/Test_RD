import scrapy
from s_test_rd.items import STestRdItem

class RDSpider(scrapy.Spider):
    name = "spider_test"
    start_urls = input('Введите ссылки:').split(', ')

    def parse(self, response):
        yield response.follow(response.css('a.UnderlineNav-item ::attr(href)').getall()[1], callback=self.parse)
        for link in response.xpath('//a[@class="d-inline-block"]/@href').getall():
            yield response.follow(link, callback=self.parse_info)


    # def parse_ch(self, response):
        # page_changelog = response.xpath('//a[@class="Link--primary d-flex no-underline"]/@href').get()
        # if page_changelog is not None:
        #     page_changelog = response.urljoin(page_changelog)
        #     yield scrapy.Request(page_changelog)
        # item = STestRdItem()
        # item = response.xpath('//div[@class="markdown-body my-3"]/p').getall()
        # return item

    def parse_info(self, response):
        item = STestRdItem()
        item_1 = STestRdItem()
        item_2 = STestRdItem()
        item['name_rep'] = response.xpath('//a[@data-pjax="#repo-content-pjax-container"]/text()').extract_first()
        item['about'] = response.xpath('//p[@class="f4 my-3"]/text()').get()
        item['link'] = response.xpath('//a[@class="text-bold"]/@href').get()
        item['stars'] = response.xpath('//span[@class="Counter js-social-count"]/@title').get()
        item['forks'] = response.xpath('//span[@class="Counter"]/@title').get()
        item['watching'] = response.xpath('//div[@class="mt-2"]//strong/text()').extract()[1]
        item['commits'] = response.xpath('//span[@class="d-none d-sm-inline"]//strong/text()').get()
        item_1['author_commit'] = response.xpath('//a[@class="commit-author user-mention"]/text()').get()
        item_1['title_commit'] = response.xpath('//a[@class="Link--primary markdown-title"]/@title').get()
        item_1['datetime_commit'] = response.xpath('//relative-time[@class="no-wrap"]/@datetime').get()
        item['info_last_commit'] = item_1
        item['release'] = response.xpath('//a[@class="Link--primary no-underline"]//span/@title').get()
        item_2['version'] = response.xpath('//span[@class="css-truncate css-truncate-target text-bold mr-2"]/text()').get()
        item_2['datetime_release'] = response.xpath('//div[@class="text-small color-fg-muted"]//relative-time[@class="no-wrap"]/@datetime').get()
        item_2['changelog'] = response.xpath('//a[@class="Link--primary d-flex no-underline"]/@href').get()
        item['info_last_release'] = item_2
        yield item

