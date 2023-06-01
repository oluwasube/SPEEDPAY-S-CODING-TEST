from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from models.user import User


transactions = Blueprint('transactions', __name__)


@transactions.route('/deposit', methods=['POST'])
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
    User.save(commit=True)

    return jsonify({'message': 'Deposit successful', 'balance': current_user.balance}), 200


@transactions.route('/withdraw', methods=['POST'])
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

    User.save(commit=True)

    return jsonify({'message': 'Withdrawal successful', 'balance': current_user.balance}), 200


@transactions.route('/balance', methods=['GET'])
@jwt_required()
def balance():
    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)

    return jsonify({'balance': current_user.balance}), 200


@transactions.route('/transfer', methods=['POST'])
@jwt_required()
def transfer():
    amount = request.json.get('amount')
    account_number = request.json.get('account_number')

    if not amount or not account_number:
        return jsonify({'message': 'Missing amount or account number'}), 400

    current_user_id = get_jwt_identity()
    current_user = User.query.get(current_user_id)
    recipient = User.query.filter_by(account_number=account_number).first()

    if not recipient:
        return jsonify({'message': 'Recipient account not found'}), 400

    if current_user.balance < amount:
        return jsonify({'message': 'Insufficient balance'}), 400

    current_user.balance -= amount
    recipient.balance += amount
    User.save(commit=True)

    return jsonify({'message': 'Transfer successful', 'balance': current_user.balance}), 200
