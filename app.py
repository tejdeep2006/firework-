from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, static_folder='static', static_url_path='')

@app.route('/')
def index():
    return render_template('index.html')

# Serve static files with the correct MIME types
@app.route('/static/<path:path>')
def serve_static(path):
    return send_from_directory('static', path)

# Handle favicon.ico requests
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
