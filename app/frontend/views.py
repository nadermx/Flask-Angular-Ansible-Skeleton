# -*- coding: utf-8 -*-
from flask import Blueprint, jsonify, render_template

mod = Blueprint('frontend', __name__)

PER_PAGE = 20

@mod.route('/')
def sign_up():
    return render_template('index.html')

@mod.route('/')
def sign_out():
    return render_template('index.html')

@mod.route('/')
def index():
    return render_template('index.html')