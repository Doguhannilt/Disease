# app.py
from flask import Flask, render_template, request
import prediction  # Import your prediction module (the modified .py file)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return "No file uploaded!", 400

    file = request.files['file']
    if file.filename == '':
        return "No selected file!", 400

    content = file.read().decode('utf-8')
    predictions = prediction.predict_diseases(content)

    # Return the predictions as a comma-separated string
    return ",".join(predictions)

if __name__ == '__main__':
    app.run(debug=True)
