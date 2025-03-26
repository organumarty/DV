from flask import Flask, send_from_directory, send_file
import os

app = Flask(__name__)

# Set the path to the Desktop folder
DESKTOP_FOLDER = os.path.expanduser('~/Desktop')

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.route('/ALLDAY.zip')
def serve_zip():
    return send_from_directory('.', 'ALLDAY.zip')

if __name__ == '__main__':
    print("Starting server...")
    app.run(host='0.0.0.0', port=8081)
