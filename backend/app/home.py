"""
All Main Page routes are defined here

"""

from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required ,current_user
from .models import User
from .models import Waitlist
from .models import Product
from .app import db


home_bp = Blueprint('home_bp', __name__)

@home_bp.route('/Home', methods = ['POST' , 'GET'])
def home():
    if current_user.is_active() and request.method == 'POST':
        # fetching data from frontend
        data = request.get_json()
        threshold = data['threshold']
        pid = data['pid']
        id = current_user.id
        #print(threshold)
        #print(pid)
        #print(id)
        # fetching product details from table
        prod = Products.query.filter_by(pid=pid).first()
        if threshold == "":
            return "enter a non-empty value!"
        else:
            # value should be in range of 30% to 100%
            # lower = params['lower_price'] * int(prod.mrp[1:])
            lower = 0.3 * int(prod.mrp[1:])
            if int(threshold) >= lower and int(threshold) <= int(prod.mrp[1:]):
                qe = Waitlist.query.filter((Waitlist.id == id) , (Waitlist.pid == pid)).first()
                #if current request is not present in Waitlist
                if qe is None:
                    entry = Waitlist(id=id, pid=pid, threshold=threshold)
                    db.session.add(entry)
                    db.session.commit()
                    return "True"
                #if user have already set the threshold before
                else:
                    return "You already have this item in your waitlist.Check your waitlist to edit threshold."
            else:
                return "Enter a value in range!"
    #if user not logged in and request is POST
    if current_user.is_active()==false and request.method == 'POST':
        return "login first!"
    return render_template("index.html", token="Hello   world")

