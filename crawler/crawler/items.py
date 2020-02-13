# -*- coding: utf-8 -*-
# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    items.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.1337.ma>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/13 22:24:33 by archid-           #+#    #+#              #
#    Updated: 2020/02/13 22:26:40 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class CrawlerItem(scrapy.Item):

    date = scrapy.Field()
    url = scrapy.Field()
    title = scrapy.Field()
    author = scrapy.Field()
    summary = scrapy.Field()
    body = scrapy.Field()
    tags = scrapy.Field()
