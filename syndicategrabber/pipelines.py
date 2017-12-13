# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import datetime

import PyRSS2Gen

class SyndicategrabberPipeline(object):
    rss_items = []

    def process_item(self, item, spider):
        rss_item = PyRSS2Gen.RSSItem(
            title = item['title'],
            link = item['url'],
            description = '<img src="{}" title="{}" />{} {}'.format(
                item['image'], item['title'], item['authors'], item['excerpt']),
            guid = item['uuid'])
        self.rss_items.append(rss_item)
        return item

    def close_spider(self, spider):
      rss_feed = PyRSS2Gen.RSS2(
          title = "Project Syndicate",
          link = "http://www.project-syndicate.org/archive",
          description = "Project Syndicate",
          lastBuildDate = datetime.datetime.now(),
          items = self.rss_items)

      rss_feed.write_xml(open("project-syndicate.rss", "w"))
