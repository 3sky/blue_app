from flask import Blueprint, render_template, request, redirect, url_for, abort
from sqlalchemy import text, desc
from flask_sqlalchemy import SQLAlchemy
import datetime
import hashlib
from jinja2 import TemplateNotFound

guest_mod = Blueprint('guest', __name__, template_folder='template')


def show(page, msg):
    try:
        return render_template('guest/%s.html' % page, message=msg)
    except TemplateNotFound:
        abort(404)


def show_user(page, msg):
    try:
        return render_template('user/%s.html' % page, message=msg)
    except TemplateNotFound:
        abort(404)