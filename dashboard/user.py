from flask import Flask, request, render_template, redirect, url_for, flash
from flask.ext.login import (LoginManager, current_user, login_required,
                            login_user, logout_user, UserMixin, RoleMixin, AnonymousUser,
                            confirm_login, fresh_login_required)

class Role(RoleMixin):
    def __init__(id, name, description, role_order):
        self.id = id
        self.name = name
        self.description = description
        self.role_order = role_order

class User(UserMixin):
    def __init__(self, id, username, password, email, first_name, last_name, active=True):
        self.id = id
        self.username = username
        self.password = password
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.active = active

    def is_active(self):
        return self.active

class UserRoles():
    def __init__(self, id):
        self.user_id = user_id
        self.role_id = role_id

