from flask import Blueprint, jsonify, json
from flask_login import current_user, login_required
from werkzeug.security import check_password_hash
from .models import db, Product
from sqlalchemy import update
wishlist_bp = Blueprint('wishlist_bp', __name__)

@wishlist_bp.route('/wishlist' , methods = ['GET','POST'])
def edit_wishlist():
