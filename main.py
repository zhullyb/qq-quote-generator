import io
from flask import Flask, render_template, request, send_file
from utils import *
from screenshot import Screenshot
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # 接收 user_id 参数, nickname 参数
    user_id = request.args.get('user_id')
    nickname = request.args.get('nickname')
    # 调用 screenshot 函数
    if request.args.get('message'):
        message = request.args.get('message')
        ss_get = ss.screenshot(message=message, user_id=user_id, nickname=nickname)
    elif request.args.get('image_url'):
        image_url = request.args.get('image_url')
        ss_get = ss.screenshot(image_url=image_url, user_id=user_id, nickname=nickname)
    if Config.RETURN_PNG:
        return send_file(io.BytesIO(ss_get), mimetype='image/png')
    else:
        return ss_get

@app.route('/quote/', methods=['GET', 'POST'])
def quote():
    # 接收 user_id 参数, nickname 参数
    user_id = request.args.get('user_id')
    nickname = request.args.get('nickname')
    avatar_url = 'https://q1.qlogo.cn/g?b=qq&nk={}&s=640'.format(user_id)
    if request.args.get('message'):
        message = request.args.get('message')
        return render_template('single-message.html', message=message, user_id=user_id, nickname=nickname, avatar_url=avatar_url)
    # 如果存在 image_url 参数，则获取 image_url 参数
    elif request.args.get('image_url'):
        image_url = request.args.get('image_url')
        return render_template('single-image.html', user_id=user_id, nickname=nickname, avatar_url=avatar_url, image_url=image_url)

if __name__ == '__main__':
    ss = Screenshot()
    app.run(host='0.0.0.0', port=Config.FLASK_RUN_PORT, debug=True)