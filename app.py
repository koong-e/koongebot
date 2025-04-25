import os
from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

@app.route('/')
def home():
    return '쿵이봇 작동 중!'

@app.route('/skill', methods=['POST'])
def skill():
    result = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": "멍멍! 쿵이예요!"
                    }
                }
            ]
        }
    }
    res = make_response(jsonify(result))
    res.headers['Content-Type'] = 'application/json; charset=utf-8'
    return res

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
