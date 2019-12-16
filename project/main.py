from flask import Blueprint, render_template
from flask_login import login_required, current_user

main =Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', account=current_user.account)

@main.route('/balance')
@login_required
def balance():
    return render_template('balance.html', account=current_user.account, balance=current_user.balance)