# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    views.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.1337.ma>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/12 14:53:57 by archid-           #+#    #+#              #
#    Updated: 2020/02/12 17:51:32 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from django.http import HttpResponse
from django.shortcuts import render

import json

def index(request):
    response = json.dumps([{}])
    return HttpResponse(response, content_type='text/json')

def get_by_title(request, title):
    pass

def get_by_tag(request):
    pass
