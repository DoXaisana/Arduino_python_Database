# Web Libray
from flask import Flask, render_template, request
# Arduino
import serial
import time
# Database (Postgres)
import psycopg2
from datetime import datetime

app = Flask(__name__)

# Set up serial connection (e.g., '/dev/tty.usbmodem14101' or 'COM3')
arduino = serial.Serial('COM1', 9600)  
time.sleep(2)  # Wait for serial connection to stabilize delay(2000)

# Database configuration (replace with your own credentials)
DB_CONFIG = {
    'dbname': 'led_status_db',
    'user': 'your_username',
    'password': 'your_password',
    'host': 'localhost',
    'port': '5432'
}

# Function to insert LED status into the database
def insert_led_status(status):
    try:
        connection = psycopg2.connect(**DB_CONFIG)
        cursor = connection.cursor()
        timestamp = datetime.now()
        cursor.execute(
            "INSERT INTO led_status (status, timestamp) VALUES (%s, %s)",(status, timestamp)
        )
        connection.commit()
    except Exception as e:
        print(f"Database error: {e}")
    finally:
        if connection:
            cursor.close()
            connection.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/led', methods=['POST'])
def led():
    status = request.form['status']
    if status == 'on':
        arduino.write(b'1')  # Send command to turn LED on
    elif status == 'off':
        arduino.write(b'0')  # Send command to turn LED off
    
    # Insert the LED status into the database
    insert_led_status(status)
    
    return 'OK'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
