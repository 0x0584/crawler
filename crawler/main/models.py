# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    models.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.1337.ma>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/12 01:20:08 by archid-           #+#    #+#              #
#    Updated: 2020/02/13 20:25:30 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from djongo import models

class Article(models.Model):
    _id = models.IntegerField(primary_key=True)
    date = models.TextField(default='')
    url = models.TextField(default='')
    title = models.TextField(default='')
    author = models.TextField(default='')
    summary = models.TextField(default='')
    body = models.ArrayField(models.TextField())
    tags = models.ArrayField(models.TextField())

    def __str__(self):
        return str(self.unique_id) + ": " + str(self.title)

    def as_json(self):
        return json.dumps([{
            'title': self.title,
            'tags': self.tags
        }])
