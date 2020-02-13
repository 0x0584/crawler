# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    views.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.1337.ma>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/12 14:53:57 by archid-           #+#    #+#              #
#    Updated: 2020/02/13 20:30:24 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from django.http import HttpResponse
from django.core import serializers

import json

from main.models import Article

def index(request):
    response = json.dumps([{}])
    return HttpResponse(response, content_type='text/json')

def get_by_title(request, word):
    if request.method == 'GET':
        try:
            # \b(\w*test\w*)\b
            print("------- debug -------", word)
            art = Article.objects.get(title=word)
            print(art)
            # response = json.dumps([{
            #     'title': art.title,
            #     'tags': art.tags
            # }])
            print("------- debug -------")
        except Exception as e:
            print("------- exception -------")
            print("err: ", vars(e))
            print(repr(e))
            print(e.args)
            response = json.dumps([{'Note': '{0}, no match found'.format(word)}])
    return HttpResponse(response, content_type='text/json')

def get_by_tag(request, t):
    pass
