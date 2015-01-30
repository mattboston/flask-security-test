#from flask_sqlalchemy import SQLAlchemy
from flask_sqlalchemy import *
#from flask import Flask, render_template, request, flash, session, redirect, url_for
from flask.ext.security import Security, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required
import datetime
import config

#dbcreds = config.get_mysql_conf()

db = SQLAlchemy()

roles_users = db.Table('roles_users',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('role_id', db.Integer(), db.ForeignKey('role.id')))

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(), unique=True)
    description = db.Column(db.String())
    role_order = db.Column(db.Integer())

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    password = db.Column(db.String)
    email = db.Column(db.String)
    first_name = db.Column(db.String)
    last_name = db.Column(db.String)
    active = db.Column(db.Enum('Y', 'N'), default='Y')
    laston = db.Column(db.DateTime)
    roles = db.relationship('Role', secondary=roles_users,
            backref=db.backref('users', lazy='dynamic')
            )

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)


