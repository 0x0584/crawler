# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    posts.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.1337.ma>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/10 18:44:23 by archid-           #+#    #+#              #
#    Updated: 2020/02/10 18:53:23 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import scrapy

class PostSpider(scrapy.Spider):
    name = 'posts'
    start_urls = [
        'https://www.bbc.com/news/world-africa-51445070'
    ]

    def parse(self, response):
        filename = 'post_%s.html' % response.url.split('/')[-1]
        with open(filename, 'wb') as f:
            f.write(response.body)
