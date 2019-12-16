from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from .models import Customers
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/login', methods=['POST'])
def login_post():
    account = request.form.get('account')
    password = request.form.get('password')

    customer = Customers.query.filter_by(account=account).first()
    if customer:
        if check_password_hash(customer.password, password):
            customer.authenticated = True
            db.session.add(customer)
            db.session.commit()
            login_user(customer, remember=True)
        return redirect(url_for("main.profile"))

    if not customer and not check_password_hash(customer.password, password):
        flash('Please check your login details and try again.')
        return redirect(url_for('auth.login'))
                
    # return redirect(url_for("main.profile"))


    # login_user(customer)

    # return redirect(url_for('main.profile'))

@auth.route('/balance', methods=['POST'])
@login_required
def balance():
    return render_template('balance.html', account=current_user.account, balance=current_user.balance)

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    account = request.form.get('account')
    balance = request.form.get('balance')
    password = request.form.get('password')

    customer = Customers.query.filter_by(account=account).first()

    if customer:
        flash('Account already exists.')
        return redirect(url_for('auth.signup'))

    new_customer = Customers(account=account, balance=balance, password=generate_password_hash(password, method='sha256'))

    db.session.add(new_customer)
    db.session.commit()

    return redirect(url_for('auth.login'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))