from flask import Blueprint, render_template
from flask_login import login_required, current_user
from . import db

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/sun')
@login_required
def sun():
    return render_template("sun.html", user=current_user)

@views.route('/mercury')
@login_required
def mercury():
    return render_template("mercury.html", user=current_user)

@views.route('/venus')
@login_required
def venus():
    return render_template("venus.html", user=current_user)
    
    