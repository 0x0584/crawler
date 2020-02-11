# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    crawler.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.1337.ma>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/10 18:44:23 by archid-           #+#    #+#              #
#    Updated: 2020/02/11 22:04:24 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from scrapy import Spider
from scrapy.http.request import Request
from urllib.parse import urljoin

from .Article import Article
from .ParseHelper import ParseHelper as Ph

class CrawlerSpider(Spider):
    name = 'crawler'
    allowed_domains = ['bbc.com']
    start_urls = ['https://www.bbc.com/news']

    # Parse start_urls and extract article links, then call parseArticle
    # on each one
    def parse(self, response):
        articles = self.prepare_urls(response)
        self.log(articles)
        for url in articles:
            yield Request(url, callback = self.parseArticle)

    # Parse an individual article
    def parseArticle(self, response):
        url = response.url
        date = response.css(Ph.parseDatetime).get()
        author = response.css(Ph.parseAuthor).get()
        title = response.css(Ph.parseTitle).get()
        summary = response.css(Ph.parseSummary).get()
        body = response.css(Ph.parseBody).getall()
        tags = response.css(Ph.parseTags).getall()
        # Some links are not articles (e.g. Videos) => ignore
        # Also some articles have no author (e.g. News reports)
        if date and title and summary and body and tags:
            body.pop(0)   # the summary is the first paragraph in the body
            article = Article(url, date, author, title, summary, body, tags)
            article.dbInsert()

    # parses the response url and returns a list of all the found urls
    def prepare_urls(self, response):
        articles = []
        urls = response.css(Ph.parseArticles).re(Ph.reArticles)
        self.log(urls)
        for url in urls:
            articles.append(urljoin(response.url, url))
        articles.extend(response.css(Ph.parseArticles).re(Ph.reLinks))
        return articles
