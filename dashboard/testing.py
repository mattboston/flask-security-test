from dashboard import app
#from flask import render_template, request, flash
from flask import Flask, flash, abort, redirect, url_for, request, render_template, make_response, json, Response, session
#from flask.ext.sqlalchemy import SQLAlchemy
import os, sys
import time
import datetime
import boto.ec2.elb
import boto
from boto.ec2 import *
import MySQLdb
from pprint import pprint
from decimal import *
import pygal
#from pygal.style import LightStyle
from pygal.style import *
from pygal import Config
import operator
import paramiko
from pssh import ParallelSSHClient

import config
from utils import *
from models import db

@app.route('/testing/')
def testing():
#    test=config.app_path()
#    session['name'] = "matt"
    if session['name']:
        test = session['name']
    else:
        test = ""
    return render_template('testing.html', test=test)

@app.route('/testing/newsession/')
def testing_newsession():
    session['name'] = datetime.datetime.now()
    return redirect("/testing/")

@app.route('/testing/users/')
def testing_users():
    if db.session.query("1").from_statement("SELECT 1").all():
        return 'It works'
    else:
        return 'Something broken'

