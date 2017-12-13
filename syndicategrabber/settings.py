# Scrapy settings for syndicategrabber project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'syndicategrabber'

SPIDER_MODULES = ['syndicategrabber.spiders']
NEWSPIDER_MODULE = 'syndicategrabber.spiders'

ITEM_PIPELINES = {
    'syndicategrabber.pipelines.SyndicategrabberPipeline':   500,
}

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'syndicategrabber (+http://www.yourdomain.com)'
