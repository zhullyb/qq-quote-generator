import io
from flask import Flask, render_template, request, send_file
import threading
from utils import *
from screenshot import Screenshot
from uuid import uuid4
app = Flask(__name__)

data_dict = {}
ss = Screenshot()

@app.after_request
def set_headers(response):
    response.headers["Referrer-Policy"] = 'no-referrer'
    return response

@app.route('/', methods=['GET', 'POST'])
def index():
    return 'see https://github.com/zhullyb/qq-quote-generator/blob/main/README.md'

def handler(ret_type):
    unique_id = str(uuid4())
    data_dict[unique_id] = request.get_json()
    ss_get = ss.screenshot(ret_type, unique_id)
    data_dict.pop(unique_id, None)
    if ret_type == 'png':
        return send_file(io.BytesIO(ss_get), mimetype='image/png')
    elif ret_type == 'base64':
        return ss_get

@app.route('/base64/', methods=['POST'])
def base64_handler_trigger():
    return handler('base64')

@app.route('/png/', methods=['POST'])
def png_handler_trigger():
    return handler('png')

@app.route('/quote/', methods=['GET', 'POST'])
def quote():
    unique_id = request.args.get('id')
    data = data_dict.get(unique_id, [])
    return render_template('main-template.html', data_list=data)
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=Config.FLASK_RUN_PORT)
