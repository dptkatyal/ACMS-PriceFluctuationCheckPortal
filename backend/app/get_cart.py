from flask import Blueprint, jsonify, json
from flask_login import current_user, login_required
from werkzeug.security import check_password_hash
from .models import db, Product
from sqlalchemy import update
prod_bp = Blueprint('prod_bp', __name__)
