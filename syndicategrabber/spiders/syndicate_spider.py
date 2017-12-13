from scrapy.selector import Selector
from scrapy.spiders import Spider
from syndicategrabber.items import SyndicategrabberItem

from subprocess import check_output

class SyndicategrabberSpider(Spider):
    name = 'syndicategrabber'
    allowed_domains = ['project-syndicate.org']
    start_urls = ['https://www.project-syndicate.org/archive']

    def parse(self, response):
        sel = Selector(response)

        articles = sel.xpath("//ol[@id='search-results']/li/article[contains(@class, 'listing')]")
        items = []
        for article in articles:
          item = SyndicategrabberItem()
          url = "http://www.project-syndicate.org/" + article.xpath("a/@href").extract()[0]
          uuid = article.xpath("a/@data-entity-id").extract()[0]
          title = article.xpath("header/h2/a/text()").extract()[0]
          authors = "".join(article.xpath("header//span[contains(@class,'byline')]//text()").extract()).strip()
          excerpt = "".join(article.xpath("header/p[@class='listing__excerpt']/text()").extract()).strip()
          image = article.xpath("header/figure/picture/source[@media='--small']/@data-srcset").extract()[0]
          #image = "https://webapi.project-syndicate.org/library/f2163b46c39a135a90a44ebaee6a8498.2-1-medium.1.jpg"

          item['url']  = url
          item['uuid'] = uuid
          item['title']  = title
          item['authors']  = authors
          item['excerpt']  = excerpt
          item['image']  = image

          items.append(item)

        return items
