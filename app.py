from flask import Flask
from datetime import datetime
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    full_name = "RAJEEV BANIYA"  
    system_username = "RAJEEV-BANIYA75"
    server_time = datetime.now().astimezone()  
    try:
        top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')
    except Exception as e:
        top_output = str(e)
    
    result =f"""
    <h1>Name: {full_name}</h1>
    <h2>Username: {system_username}</h2>
    <h2>Server Time (IST): {server_time}</h2>
    <h2>TOP output:</h2>
    <pre>{top_output}</pre>
    """

    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

