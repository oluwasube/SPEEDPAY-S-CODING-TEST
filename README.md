# SPEEDPAY-S-CODING-

from flask import Blueprint, jsonify, request

from flask_jwt_extended import jwt_required, get_jwt_identity

from models import db, User

transactions_bp = Blueprint('transactions', __name__)

@transactions_bp.route('/deposit', methods=['POST'])

@jwt_required()

def deposit():

    try:

        data = request.get_json()

        amount = data['amount']

    except KeyError:

        return jsonify({'message': 'Missing amount'}), 400

    current_user_id = get_jwt_identity()

    current_user = User.query.get(current_user_id)

    current_user.balance += amount

    db.session.commit()

    return jsonify({'message': 'Deposit successful', 'balance': current_user.balance}), 200

@transactions_bp.route('/withdraw', methods=['POST'])

@jwt_required()

def withdraw():

    try:

        data = request.get_json()

        amount = data['amount']

    except KeyError:

        return jsonify({'message': 'Missing amount'}), 400

    current_user_id = get_jwt_identity()

    current_user = User.query.get(current_user_id)

    if current_user.balance < amount:

        return jsonify({'message': 'Insufficient balance'}), 400

    current_user.balance -= amount

    db.session.commit()

    return jsonify({'message': 'Withdrawal successful', 'balance': current_user.balance}), 200

@transactions_bp.route('/balance', methods=['GET'])

@jwt_required()

def balance():

    current_user_id = get_jwt_identity()

    current_user = User.query.get(current_user_id)

    return jsonify({'balance': current_user.balance}), 200

@transactions_bp.route('/transfer', methods=['POST'])

@jwt_required()

def

