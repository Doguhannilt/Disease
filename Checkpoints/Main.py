from flask import Flask, request
from flask_cors import CORS
import sys
from werkzeug.serving import make_server
import atexit
from TheSystem import run_the_system  # Import the run_the_system function

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def predict_disease():
    
    print("Received POST request")  # For debugging: Check if the backend receives the request

    if 'file' not in request.files:
        return 'No file part', 400

    file = request.files['file']
    if file.filename == '':
        return 'No selected file', 400

    file_path = 'C:/Users/doguy/Desktop/Health/selected_diseases.txt'
    try:
        file.save(file_path)
    except Exception as e:
        return f'Error saving the file: {e}', 500

    # Perform disease prediction using the content of the file (you need to implement this part)
    # For demonstration purposes, let's assume the prediction result is 'Vertigo'
    prediction_result = 'Vertigo'

    # Stop the server after processing the request successfully
    stop_server()

    return prediction_result

def stop_server():
    """
    Stop the Flask server when called from a request.
    This function uses werkzeug.serving.make_server to stop the server gracefully.
    """
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError('Not running with the Werkzeug Server')
    func()

if __name__ == '__main__':
    # Register run_the_system function as an exit handler
    atexit.register(run_the_system)

    # Run the Flask application using make_server to enable graceful stopping
    server = make_server('127.0.0.1', 5000, app)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        # Gracefully handle keyboard interrupt
        print("Stopping the server...")
