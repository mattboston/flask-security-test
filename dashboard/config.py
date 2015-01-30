#!/usr/bin/python
# vim: set expandtab:
import os

def app_path():
    path = os.path.dirname(os.path.abspath(__file__))
    return path

def get_mysql_conf():
    mysql_host = 'localhost'
    mysql_user = 'dbuser'
    mysql_pass = 'dbpass'
    mysql_db   = 'mydb'
    return { 'mysql_host' : mysql_host, 'mysql_user' : mysql_user, 'mysql_pass' : mysql_pass, 'mysql_db' : mysql_db }

