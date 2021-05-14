from flask import Blueprint, Response, redirect, render_template, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash, generate_password_hash
from . import models

auth = Blueprint('auth', __name__)

@auth.route('/')
def login():
    return render_template('login.html')

@auth.route('/.well-known/acme-challenge/<challenge>')
def letsencrypt_check(challenge):
    challenge_response = {
       "SyVlwQEXFZDlHUzT28Ko6azone2j2hRuROOT5jlDDk0":"SyVlwQEXFZDlHUzT28Ko6azone2j2hRuROOT5jlDDk0.CsnZA_XCWM39H5F1SjCSbq5yGPswgizWR5WLnn6aoUQ",
    }
    return Response(challenge_response[challenge], mimetype='text/plain')

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    print("+ Email: {} tries to connect".format(email))
    user = models.User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password, password):
        print("- Email: {} failed to connect".format(email))
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)
    return redirect(url_for('webcam.live'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))
