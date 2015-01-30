from dashboard import app
#from flask import render_template, request, flash
from flask import Flask, flash, abort, redirect, url_for, request, render_template, make_response, json, Response, session
from flask import g
import os, sys
import time
import datetime
import boto.ec2.elb
import boto
from boto.ec2 import *
import MySQLdb
from pprint import pprint
from re import *

# import our custom modules
import config
from auth import *
from utils import *
from clients import *
from backup import *
from billing import *
from restore import *
from maint import *
from stats import *
from testing import *

#app.jinja_env.globals['current_time'] = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')

@app.route('/')
def index():
#    g.currenttime = current_time()
#    app.jinja_env.globals['current_time'] = current_time()
#    return render_template('index.html', currenttime=currenttime)
    return render_template('index.html')

