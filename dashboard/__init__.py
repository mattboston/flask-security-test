#from dashboard import app
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)
app.secret_key = 'asdf'
import config
dbcreds = config.get_mysql_conf()
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql://%s:%s@%s/%s" % (dbcreds['mysql_user'],dbcreds['mysql_pass'],dbcreds['mysql_host'],dbcreds['mysql_db'],)

from models import db
db.init_app(app)

import dashboard.routes
