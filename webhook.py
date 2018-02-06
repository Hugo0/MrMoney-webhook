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
    print('--------------------Request:----------------------')
    print(json.dumps(req, indent = 4))
    res = processRequest(req)
    res = json.dumps(res, indent = 4)
    print('/n ------------------------------------------------' + res )
    r = make_respons(res)
    r.headers['Content-Type'] = 'application/json'
    return r
	
def processRequest(req):
	if req not in ActionList:
		return {}
	else:
	    func_index = ActionList.index(req)
	    func_list[req](req)

def getStockValue(req):
    print(1)
    result = req.get('result')
    parameters = result.get('parameters')
    stock = parameters.get('Stock')
    stock_prices = {Apple:'102,5', Microsoft:'34,7', Google: '1001,56'}
    current_price = stock_prices[stock]
	
    speech = 'The current price of this stock is ' + current_price + '$'
    print('----------Result:------------')
    print(speech)
    return {
        'speech': speech,
        'displayText': speech,
    }
	
def giveFinancialTip(req):
	return 'earn more money'
	
	
def makeWebhookResult(req):
    result = req.get('result')
    parameters = result.get('parameters')
    name = parameters.get('Stock')
    speech = 'The Stock is' + name + ' lol'
    print('Response123:')
    print(speech)
    return {
        'speech': speech,
        'displayText': speech,
    }

ActionList = ['Stock', 'FinancialTip',]
func_list = {'Stock':getStockValue, 'FinancialTip' :giveFinancialTip,}

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=True, port=port, host='0.0.0.0')
