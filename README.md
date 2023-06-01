### API installation

To install and run this Python application, follow the steps below:

1. Clone the API repository to your local machine.
2. Open your terminal and navigate to the directory where the cloned application is located.
3. create a virtual environment on Linux or Windows gitbash terminal using the command:`python3 -m venv env`
4. Activate the virtual environment with the command below: `source/env/bin/activate`
5. Install the required dependencies by running the following command:
`pip install -r requirements.txt`.
6. Create a `.env` file in the root folder and define the following variables:
    `SECRET_KEY:` Set it to a value representing the desired key.
    `JWT_SECRET_KEY:`Set it to a value representing the desired key.
7.  cd into the api repository, Run the application using the following command:`python app.py`

Upon successful execution, a message will be displayed in the console indicating that the server is running on the specified port and the database connection has been established.

Note: Make sure you have Python and pip installed on your machine before proceeding with the above steps.