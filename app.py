from flask import Flask
import os
from datetime import datetime
import pytz
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    # Get the system username
    username = os.getlogin()
    # Get current server time in IST
    ist_time = datetime.now(pytz.timezone('Asia/Kolkata')).strftime('%Y-%m-%d %H:%M:%S')
    # Get top command output
    top_output = subprocess.getoutput('top -b -n 1')
    # Return the formatted response
    return f"""
    <h1>System Info</h1>
    <p>Name - Your Full Name</p>
    <p>Username - {username}</p>
    <p>Server Time in IST - {ist_time}</p>
    <pre>{top_output}</pre>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
