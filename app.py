from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "쿵이봇 작동 중!"

@app.route('/skill', methods=['POST'])
def skill():
    res = {
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
    return jsonify(res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
