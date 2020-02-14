# -*- coding: utf-8 -*-
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    pipelines.py                                       :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.1337.ma>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/13 22:41:48 by archid-           #+#    #+#              #
#    Updated: 2020/02/14 13:25:18 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import logging
import pymongo

class CrawlerPipeline(object):

    collection_name = 'Articles'

    def __init__(self, mongo_uri, mongo_db):
        self.mongo_uri = mongo_uri
        self.mongo_db = mongo_db

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            mongo_uri=crawler.settings.get('MONGO_URI'),
            mongo_db=crawler.settings.get('MONGO_DATABASE')
        )

    def open_spider(self, spider):
        self.client = pymongo.MongoClient(self.mongo_uri)
        self.db = self.client[self.mongo_db]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].update(dict(item), dict(item), upsert=True)
        logging.debug("added to MongoDB")
        return item
