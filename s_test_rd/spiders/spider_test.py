import scrapy
#from s_test_rd.items import STestRdItem

class RDSpider(scrapy.Spider):
    name = "spider_test"
    start_urls = ['https://github.com/scrapy', 'https://github.com/celery/']


    def parse(self, response):
        yield response.follow(response.css('a.UnderlineNav-item ::attr(href)').getall()[1], callback=self.parse)
        for link in response.xpath('//a[@class="d-inline-block"]/@href').getall():
            yield response.follow(link, callback=self.parse_info)


    def parse_info(self, response):
        yield {
            'name_rep': response.xpath('//a[@data-pjax="#repo-content-pjax-container"]/text()').extract_first(),
            'about': response.xpath('//p[@class="f4 my-3"]/text()').get().strip(),
            'link': response.xpath('//a[@class="text-bold"]/@href').get(),
            'stars': response.xpath('//span[@class="Counter js-social-count"]/@title').get(),
            'forks': response.xpath('//span[@class="Counter"]/@title').get(),
            'watching': response.xpath('//div[@class="mt-2"]//strong/text()').extract()[1],
            'commits': response.xpath('//span[@class="d-none d-sm-inline"]//strong/text()').get(),
            'info_last_commit': {'author_commit': response.xpath('//a[@class="commit-author user-mention"]/text()').get(),
                                 'title_commit': response.xpath('//a[@class="Link--primary markdown-title"]/@title').get(),
                                 'datetime_commit': response.xpath('//relative-time[@class="no-wrap"]/@datetime').get()},
            'release': response.xpath('//a[@class="Link--primary no-underline"]//span/@title').get(),
            'info_last_release': {'version': response.xpath('//span[@class="css-truncate css-truncate-target text-bold mr-2"]/text()').get(),
                                  'datetime_release': response.xpath('//div[@class="text-small color-fg-muted"]//relative-time[@class="no-wrap"]/@datetime').get()}
            # #l_3['changelog'] = ????????

        }


