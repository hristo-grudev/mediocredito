BOT_NAME = 'mediocredito'

SPIDER_MODULES = ['mediocredito.spiders']
NEWSPIDER_MODULE = 'mediocredito.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'mediocredito.pipelines.MediocreditoPipeline': 100,

}
