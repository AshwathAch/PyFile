from flask import Flask, request
import motor_control

app = Flask(__name__)

@app.route('/')
def index():
    # Serve the HTML page
    return open('index.html').read()

@app.route('/control_motor')
def control_motor():
    action = request.args.get('action')

    if action == 'forward':
        motor_control.forward()  # Call a function in motor_control.py to move forward
        return 'Forward command sent'
    elif action == 'reverse':
        motor_control.reverse()  # Call a function in motor_control.py to move reverse
        return 'Reverse command sent'
    else:
        return 'Invalid action', 400  # Return error if the action is not recognized

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)  # Run the Flask app on port 80
