from dashboard import app
#from flask import render_template, request, flash
from flask import Flask, flash, abort, redirect, url_for, request, render_template, make_response, json, Response, session
#from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required
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


#@app.route('/login')
#def login():
#    return render_template('login.html')
#
#@app.route('/signin', methods=['GET','POST'])
#def signin():
#    if request.method == 'POST':
#        session['name'] = request.form['username']
#        return redirect('/testing/')
#    else:
#        return redirect('/login')

@app.route('/signedin')
@login_required
def signedin():
    return "You're signed in"
