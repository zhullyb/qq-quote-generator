import io
from flask import Flask, render_template, request, send_file
import threading
from utils import *
from screenshot import Screenshot
from uuid import uuid4
app = Flask(__name__)

data_dict = {}

@app.after_request
def set_headers(response):
    response.headers["Referrer-Policy"] = 'no-referrer'
    return response

@app.route('/', methods=['GET', 'POST'])
def handler():
    unique_id = str(uuid4())
    data_dict[unique_id] = request.get_json()
    ss_get = ss.screenshot(unique_id)
    data_dict.pop(unique_id, None)
    if Config.RETURN_PNG:
        return send_file(io.BytesIO(ss_get), mimetype='image/png')
    else:
        return ss_get

@app.route('/quote/', methods=['GET', 'POST'])
def quote():
    unique_id = request.args.get('id')
    data = data_dict.get(unique_id, [])
    return render_template('main-template.html', data_list=data)
    
if __name__ == '__main__':
    # init headless browser
    ss = Screenshot()
    
    app.run(host='0.0.0.0', port=Config.FLASK_RUN_PORT)
