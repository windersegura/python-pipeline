from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/payment')
def payment():
    return jsonify({
        'status':'success',
        'message':'Payment processed successfull'})

@app.route('/api/health')
def health():
    return jsonify({"healthy": True})

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)


