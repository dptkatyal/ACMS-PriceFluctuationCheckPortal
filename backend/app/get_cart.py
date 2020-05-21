from flask import Blueprint, jsonify, json
from flask_login import current_user, login_required
from werkzeug.security import check_password_hash
from .models import db, Product
from .models import db, Waitlist
from .models import db, User
from sqlalchemy import update
cart_bp = Blueprint('cart_bp', __name__)

@cart_bp.route('/customer' , methods = ['GET'])
def get_cart():
    id = current_user.id
    prod = []
    mylist = Waitlist.query.filter(Waitlist.id == id).all()
    for pr in mylist:
        data = Product.query.filter(Product.pid == pr.pid).first()
        dict = {'pid':data.pid , 'name':data.name , 'mrp':data.mrp , 'price':data.price, 'img_file':data.img_file , 'slug': data.slug , 'description':data.description}
        prod.append(dict)
    return jsonify(prod)
