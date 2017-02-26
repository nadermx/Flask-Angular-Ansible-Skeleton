import sys
from flask import (Blueprint, request, jsonify, redirect)
from app import models
import json
import mailgun

mod = Blueprint('users', __name__, url_prefix='/users')


@mod.route('/signup', methods=['POST'])
@models.db_session
def signup():
    if request.method == 'POST':
        data = request.json
        try:
            username = data['username']
            password = data['password']
        except:
            return jsonify(status='missing username or password')
        user = models.User.get(username=username)
        if user:
            status = 'already registered username or email'
            return jsonify(status=status)
        email = data['email'].lower()
        user = models.User.get(email=email)
        if user:
            status = 'already registered username or email'
            return jsonify(status=status)
        try:
            user = models.User(username=username, email=email)
            user.hash_password(password)
            models.commit()
            mailgun.send_verification_email(email, user.generate_auth_email_token().decode('ascii'))
            token = user.generate_auth_token()
            status = True
        except:
            return jsonify(status='something went wrong')
        return jsonify(status=status, token=token.decode('ascii'))



@mod.route('/lost_password', methods=['POST'])
@models.db_session
def lost_password():
    data = json.loads(request.data)
    try:
        to_find = data['email_username']
    except:
        return jsonify(error='username or email not supplied')
    user = False
    if len(to_find) <= 20:
        user = models.User.get(username=to_find)
    if not user:
        user = models.User.get(email=to_find.lower())
    if not user:
        return jsonify(error='No user')
    name = user.name
    username = user.username
    email = user.email
    token = user.generate_auth_email_token().decode('ascii')
    mailgun.reset_password_email(name, username, email, token)
    return jsonify(status=True)

@mod.route('/reset_password', methods=['PUT'])
@models.db_session
def reset_password():
    try:
        token = request.headers['Token']
    except:
        return jsonify(error='No Token')
    user = models.User.verify_auth_token(token)
    if not user:
        return jsonify(error='Error')
    password = json.loads(request.data)['password']
    user.hash_password(password)
    models.commit()
    return jsonify(status=True)


@mod.route('/login', methods=['POST'])
@models.db_session
def login():
    data = request.json
    models.commit()
    try:
        username = data['username']
        password = data['password']
    except:
        return jsonify(status='username or password not supplied')
    try:
        user = models.User.get(username=username)
        if not user:
            user = models.User.get(username=username.lower())
            if not user:
                user = models.User.get(email=username.lower())
                if not user:
                    return jsonify(status='no user exists')
        if user.verify_password(password):
            token = user.generate_auth_token()
            token = token.decode('ascii')
            status = True
        else:
            return jsonify(status='Invalid Password')
    except:
        return jsonify(status='something went wrong')
    return jsonify(status=status, token=token)
