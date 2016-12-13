#encoding: utf-8
from pymongo import MongoClient
from scrapy.conf import settings
client = MongoClient(
            settings['MONGODB_SERVER'],
            settings['MONGODB_PORT']
        )
News_fenghDB = client[settings['MONGODB_DB']]
collect_fengh_161212 = News_fenghDB[settings['MONGODB_COLLECTION']]