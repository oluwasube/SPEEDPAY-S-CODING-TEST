# API Installation

To install and run this Python application, follow the steps below:

1. Clone the API repository to your local machine.
2. Open your terminal and navigate to the directory where the cloned application is located.
3. Create a virtual environment using the following command:
   - For Linux or Windows Git Bash Terminal: `python3 -m venv env`
4. Activate the virtual environment with the command below:
   - For Linux or Windows Git Bash Terminal: `source env/bin/activate`
5. Install the required dependencies by running the following command:`pip install -r requirements.txt`.
6. Create a `.env` file in the root folder and define the following variables:

- `SECRET_KEY`: Set it to a value representing the desired key.
- `JWT_SECRET_KEY`: Set it to a value representing the desired key.

7. Change your directory to the `api` repository and run the application using the following command:`python3 app.py`

Upon successful execution, a message will be displayed in the console indicating that the server is running on the specified port and the database connection has been established.

**Note:** Make sure you have Python and pip installed on your machine before proceeding with the above steps.

# Endpoint Documentation

## Auth API Documentation

This documentation provides information about the Auth API endpoints.

**Register**:
Registers a new user.

Endpoint: `api/v1/register`

Method: `POST`

**Request Body**:
The request body should be a JSON object with the following properties:

- `username` (string, required): The username of the user.
- `password` (string, required): The password of the user.
- `firstname` (string, required): The first name of the user.
- `lastname` (string, required): The last name of the user.
- `email` (string, required): The email address of the user.

**Example**:

```
{
  "username": "john_doe",
  "password": "password123",
  "firstname": "John",
  "lastname": "Doe",
  "email": "john.doe@example.com"
}

```

**Response(success)**:

```{
  "message": "User registered successfully.",
  "account_number": "123456"
}
```

**Login**:
Authenticates a user and returns an access token.

Endpoint:`api/v1/login`

Method: `POST`

**Request Body**:
The request body should be a JSON object with the following properties:

-`username` (string, required): The username of the user. -`password` (string, required): The password of the user.

**Example**:

```
{
  "username": "john_doe",
  "password": "password123"
}

```

**Response(success)**:

```
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwiaWF0IjoxNjIzNzgxNTI0LCJleHAiOjE2MjM3ODUxMjR9.PA-H9y8I0D_q__kgGAAE5ztzPofeHLxK8UxTCTigdW4"
}

```

## Transfer API Documentation

**Deposit**:

This endpoint allows the authenticated user to deposit an amount to their account balance.

Endpoint: `api/v1/deposit`

Method: `POST`

Protected: Yes `(JWT required)`

**Request Body**:
The request body must be a JSON object with the following properties:

- `amount` (required): The amount to be deposited.

**Example**:

```{
  "amount": 100.0
}
```

**Response(success)**:

```{
  "message": "Deposit successful",
  "balance": 1500.0
}

```

**Withdraw**:
This endpoint allows the authenticated user to withdraw an amount from their account balance.

Endpoint: `api/v1/withdraw`

Method: `POST`

Protected: Yes `(JWT required)`

**Request Body**:
The request body must be a JSON object with the following properties:

- `amount` (required): The amount to be withdrawn.
  **Example**:

```{
  "amount": 50.0
}

```

**Response(success)**:

```
{
  "message": "Withdrawal successful",
  "balance": 1450.0
}

```

**Balance**:
This endpoint allows the authenticated user to retrieve their current account balance.
Endpoint: `api/v1/balance`

Method: `GET`

Protected: Yes `(JWT required)`
**Response(success)**:

```
{
  "balance": 1500.0
}
```

**Transfer**:

This endpoint allows the authenticated user to transfer an amount from their account to another user's account.

Endpoint:`api/v1/transfer`

Method: `POST`

Protected: Yes `(JWT required)`

**Request Body**:
The request body must be a JSON object with the following properties:

- `amount` (required): The amount to be transferred.
- `account_number `(required): The account number of the recipient.
  **Example**:

```{
  "amount": 200.0,
  "account_number": "123456"
}

```

**Response(success)**:

```
{
  "message": "Transfer successful",
  "balance": 1300.0
}

```
