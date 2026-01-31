from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return jsonify({
        "message": "Hello, World! Welcome to the DevOps Demo.",
        "status": "success"
    })

@app.route('/health')
def health_check():
    return jsonify({
        "status": "healthy"
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
