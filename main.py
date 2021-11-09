import json
import os
import ipinfo

from flask import Flask
from flask import request
app = Flask(__name__)

RESPONSE = os.environ["RESPONSE"]
access_token = "23ffa8809593a8"
handler = ipinfo.getHandler(access_token)

@app.route("/status")
def root():
	ret = {
		'result': RESPONSE
	}

	return json.dumps(ret)

@app.route("/ip")
def ip():
	ip_address = request.remote_addr
	details = handler.getDetails(ip_address)
	data = {
		"ip": details.ip,
		"city": details.city,
		"state": details.region
	}
	return json.dumps(data)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)