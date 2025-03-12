# from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify, send_file
# from werkzeug.security import generate_password_hash, check_password_hash
# import json
# import os

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'  # Change this to a random secret key

# # In-memory storage for demonstration purposes
# users_db = {
#     'user1': {
#         'password': generate_password_hash('password123')
#     }
# }
# flights = []

# @app.route('/')
# def index():
#     if 'username' in session:
#         return redirect(url_for('welcome'))
#     return render_template('index.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         user = users_db.get(username)
        
#         if user and check_password_hash(user['password'], password):
#             session['username'] = username
#             return redirect(url_for('welcome'))
#         else:
#             flash('Invalid username or password')
#     return render_template('login.html')

# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         password = request.form['password']
#         role = request.form['role']
#         gender = request.form['gender']
#         email = request.form['email']
#         telephone = request.form['telephone']
        
#         if username in users_db:
#             flash('Username already exists')
#             return redirect(url_for('register'))
        
#         hashed_password = generate_password_hash(password)
#         users_db[username] = {
#             'password': hashed_password,
#             'role': role,
#             'gender': gender,
#             'email': email,
#             'telephone': telephone
#         }
#         flash('Account created successfully!')
#         return redirect(url_for('login'))
#     return render_template('register.html')

# @app.route('/welcome')
# def welcome():
#     if 'username' not in session:
#         return redirect(url_for('login'))
#     username = session['username']
#     return render_template('welcome.html', username=username)

# @app.route('/logout')
# def logout():
#     session.pop('username', None)
#     return redirect(url_for('login'))

# @app.route('/submit', methods=['POST'])
# def submit():
#     if request.method == 'POST' and 'username' in session:
#         # Extract data from the form
#         flight_data = {
#             'date': request.form['date'],
#             'reference_number': request.form['refNo'],
#             'supervisor': request.form['supervisor'],
#             'flight': request.form['flight'],
#             'zone': request.form['zone'],
#             'passenger_counts': {
#                 'paid': int(request.form['paid']),
#                 'diplomats': int(request.form['diplomats']),
#                 'infants': int(request.form['infants']),
#                 'not_paid': int(request.form['notPaid']),
#                 'field_card_qr': int(request.form['paidCardQr']),
#                 'refunds': int(request.form['refunds']),
#                 'deposited': int(request.form['deportees']),
#                 'transit': int(request.form['transit']),
#                 'waivers': int(request.form['waivers']),
#                 'prepaid_bank': int(request.form['prepaidBank']),
#                 'round_trip': int(request.form['roundTrip']),
#                 'late_payment': int(request.form['latePayment'])
#             },
#             'remarks': request.form['remarks']
#         }
#         # Calculate total attended by summing all passenger counts and subtracting refunds
#         total_attended = sum(flight_data['passenger_counts'].values()) - flight_data['passenger_counts']['refunds']
#         flight_data['total_attended'] = total_attended
        
#         # Add the new flight data to the in-memory storage
#         flights.append(flight_data)
#         # Return the updated list of flights
#         return jsonify(flights)
#     else:
#         return redirect(url_for('login'))

# @app.route('/verify', methods=['POST'])
# def verify():
#     if request.method == 'POST' and 'username' in session:
#         # Extract the report ID and verification data from the request
#         report_id = request.form['id']
#         verification_data = {
#             'iics_infant': request.form['iicsInfant'],
#             'iics_adult': request.form['iicsAdult'],
#             'iics_total': request.form['iicsTotal'],
#             'gia_infant': request.form['giaInfant'],
#             'gia_adult': request.form['giaAdult'],
#             'gia_total': request.form['giaTotal'],
#             'iics_total_difference': request.form['iicsTotalDifference'],
#             'gia_total_difference': request.form['giaTotalDifference']
#         }
#         # Find the report by ID and update its verification status
#         for report in flights:
#             if report.get('id') == report_id:
#                 report['verified'] = True
#                 report['verification_data'] = verification_data
#                 break
#         # Return the updated list of flights
#         return jsonify(flights)
#     else:
#         return redirect(url_for('login'))

# @app.route('/update', methods=['POST'])
# def update():
#     if request.method == 'POST' and 'username' in session:
#         # Extract the report ID and update data from the request
#         report_id = request.form['id']
#         update_data = {
#             'paid': int(request.form['paid']),
#             'diplomats': int(request.form['diplomats']),
#             'infants': int(request.form['infants']),
#             'not_paid': int(request.form['notPaid']),
#             'paid_card_qr': int(request.form['paidCardQr']),
#             'refunds': int(request.form['refunds']),
#             'deposited': int(request.form['deportees']),
#             'transit': int(request.form['transit']),
#             'waivers': int(request.form['waivers']),
#             'prepaid_bank': int(request.form['prepaidBank']),
#             'round_trip': int(request.form['roundTrip']),
#             'late_payment': int(request.form['latePayment'])
#         }
#         # Find the report by ID and update its data
#         for report in flights:
#             if report.get('id') == report_id:
#                 report.update(update_data)
#                 break
#         # Return the updated list of flights
#         return jsonify(flights)
#     else:
#         return redirect(url_for('login'))

# @app.route('/download', methods=['GET'])
# def download():
#     if 'username' in session:
#         # Create a JSON file from the in-memory storage
#         filename = 'flights.json'
#         with open(filename, 'w') as f:
#             json.dump(flights, f, indent=4)
#         # Send the JSON file to the client for download
#         return send_file(filename, as_attachment=True, mimetype='application/json')
#     else:
#         return redirect(url_for('login'))

# if __name__ == '__main__':
#     app.run(debug=True)






from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify, send_file
from werkzeug.security import generate_password_hash, check_password_hash
import mysql.connector
from mysql.connector import Error
import json

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Change this to a random secret key

# Configure MySQL connection
db_config = {
    'user': 'jawo',
    'password': 'abc_123',
    'host': 'localhost',
    'database': 'ccdb',
    'raise_on_warnings': True
}

# Establish a connection to the MySQL database
try:
    db = mysql.connector.connect(**db_config)
    app.config['db'] = db
except Error as e:
    print("Error while connecting to MySQL", e)

# @app.before_first_request
# def setup():
    # Create tables if they do not exist
    cursor = app.config['db'].cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
           id INT AUTO_INCREMENT PRIMARY KEY,
           username VARCHAR(255) NOT NULL UNIQUE,
           password VARCHAR(255) NOT NULL,
           role VARCHAR(255) NOT NULL,
           gender VARCHAR(255),
           email VARCHAR(255),
           telephone VARCHAR(20)
       );
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS flight_data (
           id INT AUTO_INCREMENT PRIMARY KEY,
           date DATE NOT NULL,
           reference_number VARCHAR(255) NOT NULL,
           supervisor VARCHAR(255) NOT NULL,
           flight VARCHAR(255) NOT NULL,
           zone VARCHAR(255) NOT NULL,
           passenger_counts JSON NOT NULL,
           total_attended INT NOT NULL,
           remarks TEXT,
           INDEX (date)
       );
    """)
    app.config['db'].commit()

@app.route('/')
def index():
    if 'username' in session:
        return redirect(url_for('welcome'))
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        cursor = app.config['db'].cursor()
        cursor.execute("SELECT * FROM users WHERE username = %s", (username))
        user = cursor.fetchone()
        
        if user and check_password_hash(user[2], password):
            session['username'] = username
            return redirect(url_for('welcome'))
        else:
            flash('Invalid username or password')
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        role = request.form['role']
        gender = request.form['gender']
        email = request.form['email']
        telephone = request.form['telephone']
        
        cursor = app.config['db'].cursor()
        try:
            cursor.execute("INSERT INTO users (username, password, role, gender, email, telephone) VALUES (%s, %s, %s, %s, %s, %s)", 
                 (username, generate_password_hash(password), role, gender, email, telephone))
            app.config['db'].commit()
            flash('Account created successfully!')
            return redirect(url_for('login'))
        except Error as e:
            print(e)
            flash('Username already exists')
    return render_template('register.html')

@app.route('/welcome')
def welcome():
    if 'username' not in session:
        return redirect(url_for('login'))
    username = session['username']
    return render_template('welcome.html', username=username)

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST' and 'username' in session:
        cursor = app.config['db'].cursor()
        # Extract data from the form
        flight_data = {
            'date': request.form['date'],
            'reference_number': request.form['refNo'],
            'supervisor': request.form['supervisor'],
            'flight': request.form['flight'],
            'zone': request.form['zone'],
            'passenger_counts': json.loads(request.form['passenger_counts']),
            'remarks': request.form['remarks']
        }
        # Calculate total attended by summing all passenger counts and subtracting refunds
        total_attended = sum(flight_data['passenger_counts'].values()) - flight_data['passenger_counts'].get('refunds', 0)
        flight_data['total_attended'] = total_attended
        
        # Add the new flight data to the database
        cursor.execute("""
            INSERT INTO flight_data (date, reference_number, supervisor, flight, zone, passenger_counts, total_attended, remarks)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            flight_data['date'],
            flight_data['reference_number'],
            flight_data['supervisor'],
            flight_data['flight'],
            flight_data['zone'],
            json.dumps(flight_data['passenger_counts']),
            flight_data['total_attended'],
            flight_data['remarks']
        ))
        app.config['db'].commit()
        # Return the updated list of flight_data
        cursor.execute("SELECT * FROM flight_data")
        flight_data = cursor.fetchall()
        return jsonify(flight_data)
    else:
        return redirect(url_for('login'))

@app.route('/verify', methods=['POST'])
def verify():
    if request.method == 'POST' and 'username' in session:
        # Extract the report ID and verification data from the request
        report_id = request.form['id']
        verification_data = {
            'iics_infant': request.form['iicsInfant'],
            'iics_adult': request.form['iicsAdult'],
            'iics_total': request.form['iicsTotal'],
            'gia_infant': request.form['giaInfant'],
            'gia_adult': request.form['giaAdult'],
            'gia_total': request.form['giaTotal'],
            'iics_total_difference': request.form['iicsTotalDifference'],
            'gia_total_difference': request.form['giaTotalDifference']
        }
        # Find the report by ID and update its verification status
        cursor = app.config['db'].cursor()
        cursor.execute("SELECT * FROM flight_data WHERE id = %s", (report_id))
        report = cursor.fetchone()
        if report:
            report['verified'] = True
            report['verification_data'] = verification_data
            app.config['db'].commit()
        # Return the updated list of flight_data
        cursor.execute("SELECT * FROM flight_data")
        flight_data = cursor.fetchall()
        return jsonify(flight_data)
    else:
        return redirect(url_for('login'))

@app.route('/update', methods=['POST'])
def update():
    if request.method == 'POST' and 'username' in session:
        # Extract the report ID and update data from the request
        report_id = request.form['id']
        update_data = {
            'paid': int(request.form['paid']),
            'diplomats': int(request.form['diplomats']),
            'infants': int(request.form['infants']),
            'not_paid': int(request.form['notPaid']),
            'paid_card_qr': int(request.form['paidCardQr']),
            'refunds': int(request.form['refunds']),
            'deposited': int(request.form['deportees']),
            'transit': int(request.form['transit']),
            'waivers': int(request.form['waivers']),
            'prepaid_bank': int(request.form['prepaidBank']),
            'round_trip': int(request.form['roundTrip']),
            'late_payment': int(request.form['latePayment'])
        }
        # Find the report by ID and update its data
        cursor = app.config['db'].cursor()
        cursor.execute("""
            UPDATE flight_data
            SET
            paid = %s,
            diplomats = %s,
            infants = %s,
            not_paid = %s,
            paid_card_qr = %s,
            refunds = %s,
            deposited = %s,
            transit = %s,
            waivers = %s,
            prepaid_bank = %s,
            round_trip = %s,
            late_payment = %s
            WHERE id = %s
        """, (
            update_data['paid'],
            update_data['diplomats'],
            update_data['infants'],
            update_data['not_paid'],
            update_data['paid_card_qr'],
            update_data['refunds'],
            update_data['deposited'],
            update_data['transit'],
            update_data['waivers'],
            update_data['prepaid_bank'],
            update_data['round_trip'],
            update_data['late_payment'],
            report_id
        ))
        app.config['db'].commit()
        # Return the updated list of flight_data
        cursor.execute("SELECT * FROM flight_data")
        flight_data = cursor.fetchall()
        return jsonify(flight_data)
    else:
        return redirect(url_for('login'))

@app.route('/download', methods=['GET'])
def download():
    if 'username' in session:
        # Create a JSON file from the database
        cursor = app.config['db'].cursor()
        cursor.execute("SELECT * FROM flight_data")
        flight_data = cursor.fetchall()
        filename = 'flight_data.json'
        with open(filename, 'w') as f:
            json.dump(flight_data, f, indent=4)
        # Send the JSON file to the client for download
        return send_file(filename, as_attachment=True, mimetype='application/json')
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)