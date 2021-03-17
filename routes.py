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
connection = "mongodb+srv://cluster0.lwy14.mongodb.net/snapup"
