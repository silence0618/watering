from flask import Flask, render_template, request
from relay_control import toggle_relay

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/control', methods=['POST'])
def control():
    relay_number = int(request.form['relay'])
    toggle_relay(relay_number)
    return render_template('index.html')  # Return to the control panel

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

