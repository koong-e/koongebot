from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return '쿵이봇 작동 중!'

@app.route('/skill', methods=['POST'])
def skill():
    body = request.get_json()  # 요청 JSON 받아오기
    utter = body['userRequest']['utterance']  # 사용자가 말한 내용 꺼내기

    # 간단한 로직 예시 (여기서 응답 커스터마이즈 가능)
    if '쿵이' in utter:
        text = "멍멍! 쿵이예요!"
    else:
        text = "무슨 말인지 잘 모르겠어요 🐶"

    res = {
        "version": "2.0",
        "template": {
            "outputs": [
                {
                    "simpleText": {
                        "text": text
                    }
                }
            ]
        }
    }
    return jsonify(res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
