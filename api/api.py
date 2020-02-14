# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    api.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.1337.ma>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/14 00:54:32 by archid-           #+#    #+#              #
#    Updated: 2020/02/14 02:29:36 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from flask import Flask, request
from bson import json_util
from pymongo import MongoClient

import json

app     = Flask(__name__)
conn    = MongoClient()
db      = conn.crawler_db

def json_response(blob):
    response = app.response_class(
        response=json.dumps(blob,default=json_util.default),
        status=200, mimetype='application/json')
    return response

def do_query(field, item):
    results = db['Articles'].find({field: {'$regex': item, '$options' : 'i'}})
    return json_response([foo for foo in results])

@app.route('/', methods=['GET'])
def index():
    return json_response({})

@app.route('/word/<w>', methods=['GET'])
def word(w):
    if request.method == 'GET':
        return do_query('title', w)

@app.route('/tag/<t>', methods=['GET'])
def tag(t):
    if request.method == 'GET':
        return do_query('tags', t)

@app.route('/author/<a>', methods=['GET'])
def author(a):
    if request.method == 'GET':
        return do_query('author', a)

@app.route('/text/<a>', methods=['GET'])
def text(a):
    if request.method == 'GET':
        return do_query('body', a)

if __name__ == "__main__":
    app.run(debug=True)
