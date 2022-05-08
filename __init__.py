from flask import Flask
#,session,render_template,request,redirect,url_for

# import json to load JSON data to a python dictionary
import json

# urllib.request to make a request to api
import urllib.request


app=Flask(__name__)

from weatherapi import authentication
from weatherapi import database
