import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

# Flask app should start in global lazout

app = Flask(__name__)

@app.route('/webhook', methods = ['POST'])
def webhook():
    req = request.get_json(silent = True, force = True)
    print('Request:')
    print(json.dumps(req, indent = 4))
    res = makeWebhookResult(req)
    res = json.dumps(res, indent = 4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    print('1')
    return r

def makeWebhookResult(req):
    if req.get('result').get('action') != 'Stock':
        return {}
    result = req.get('result')
    parameters = result.get('parameters')
    name = parameters.get('Stock')
    speech = 'The Stock is' + name + ' lol'
    print('Response123:')
    print(speech)
    return {
        'speech': speech,
        'displayText': speech,
        "source": 'agent',
    }

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')


