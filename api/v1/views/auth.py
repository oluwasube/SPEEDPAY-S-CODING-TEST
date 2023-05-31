from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User
from utils.Account_number import generate_account_number


auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['POST'])
def register():

    try:
        data = request.get_json()

        username = data['username']
        password = data['password']
        firstname = data['firstname']
        lastname = data['lastname']

        if not username or not password:
            return jsonify({'message': 'Username and password are required.'}), 400
        if User.query.filter_by(username=username).first():
            return jsonify({'message': 'Username already exists.'}), 400

    except:
        print('An error occurred')

    account_number = generate_account_number()
    balance = 0.0

    user = User(username=username, password=generate_password_hash(
        password), firstname=firstname, lastname=lastname,  account_number=account_number, balance=balance)
    User.save(user, commit=True)

    return jsonify({'message': 'User registered successfully.', 'account_number': account_number}), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    user = User.query.filter_by(username=username).first()

    if not user or not check_password_hash(user.password, password):
        return jsonify({'message': 'Invalid username or password.'}), 401

    access_token = create_access_token(identity=user.id)
    return jsonify({'access_token': access_token}), 200
