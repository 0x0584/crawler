# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Article.py                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.1337.ma>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/10 19:45:53 by archid-           #+#    #+#              #
#    Updated: 2020/02/11 22:00:13 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# Article is a container of the information that's crawled from the website.
# it has the typical properties, such as title and tags. And also methode(s)
# to interact with the DB
class Article:
    # list of all articles
    articles = []

    def __init__(self, url, date, author, title, summary, paragraphs, tags):
        self.date = date
        self.url = url
        self.title = title
        self.author = author
        self.summary = summary
        self.body = paragraphs
        self.tags = tags

    # TODO: Inserts the the article into the DB
    def dbInsert(self):
        print("Dump: ", vars(self))
        self.articles.append(self)
