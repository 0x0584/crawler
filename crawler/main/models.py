# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    models.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.1337.ma>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/12 01:20:08 by archid-           #+#    #+#              #
#    Updated: 2020/02/13 01:46:09 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from djongo import models

import json

class Article(models.Model):
    date = models.TextField()
    url = models.TextField()
    title = models.TextField()
    author = models.TextField()
    summary = models.TextField()
    body = models.ArrayField(models.TextField())
    tags = models.ArrayField(models.TextField(), default='foo')

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title

    # This is for basic and custom serialisation to return it to client as a JSON.
    # @property
    # def to_dict(self):
    #     data = {
    #         'url': self.url,
    #         'date': self.date,
    #         'title': self.title,
    #         'author': self.author,
    #         'summary': self.summary,
    #         'body': self.body,
    #         'tags': self.tags
    #     }
    #     return data

    # def __str__(self):
    #     return self.unique_id
