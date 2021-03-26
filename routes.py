from flask import Blueprint, request, jsonify

import json

import pymongo

import os
import sys
from pymongo import MongoClient
from bson import ObjectId


class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)


# MongoDb config
connection = "mongodb+srv://snapup:password12345@cluster0.lwy14.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
client = MongoClient(connection)
db = client['snapup']
collection = db['items']

# BluePrints connect functionality to the main component
indexRoute = Blueprint('index', __name__)
create = BluePrint('create', __name__)
# routes


@indexRoute.route('/api/items')
def index():
    return jsonify(data='something')


@createRoute.route('/api/create',  method=['POST'])
def create():


print(request.json, flush=True)
