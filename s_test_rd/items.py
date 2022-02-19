# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class STestRdItem(scrapy.Item):
    name_rep = scrapy.Field()
    about = scrapy.Field()
    link = scrapy.Field()
    stars = scrapy.Field()
    forks = scrapy.Field()
    watching = scrapy.Field()
    commits = scrapy.Field()
    info_last_commit = scrapy.Field()
    release = scrapy.Field()
    info_last_release = scrapy.Field()