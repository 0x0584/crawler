# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    api.py                                             :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: archid- <archid-@student.1337.ma>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/02/14 00:54:32 by archid-           #+#    #+#              #
#    Updated: 2020/02/14 02:05:21 by archid-          ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from flask import Flask, request, jsonify, make_response, Response
from bson import json_util
from pymongo import MongoClient

import json

app = Flask(__name__)

conn = MongoClient()
db = conn.crawler_db

@app.route('/', methods=['GET'])
def index():
    json.dumps({})

@app.route('/word/<w>', methods=['GET'])
def word(w):
    if request.method == 'GET':
        return do_query('title', w)

@app.route('/tag/<t>', methods=['GET'])
def tag(t):
    if request.method == 'GET':
        return do_query('tags', t)

def do_query(field, item):
    results = db['Articles'].find({field: {'$regex': item, '$options' : 'i'}})
    json_res = [foo for foo in results]
    response = app.response_class(
        response=json.dumps(json_res,default=json_util.default),
        status=200, mimetype='application/json')
    return response

if __name__ == "__main__":
    app.run(debug=True)
