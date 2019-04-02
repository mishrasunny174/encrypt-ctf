import os, random
from datetime import datetime
from calendar import timegm
from flask import Flask, render_template, jsonify

app = Flask(__name__)

'''
 secret_key using python3 secrets module
'''

app.secret_key = "9d367b3ba8e8654c6433379763e80c6e"

FLAG = "encryptCTF{v1rtualenvs_4re_c00l}"

@app.route('/')
@app.route('/home')
def index():
	return render_template('index.html')


@app.route('/whatsthetime')
def whatsthetime():
	return render_template('soclose.html')

@app.route('/whatsthetime/<int:what_the_timestamp>', methods=["GET", "POST"])
def getflag(what_the_timestamp):
	ts = timegm(datetime.utcnow().utctimetuple())
	if what_the_timestamp == ts:
	    return jsonify({
	        'flag': FLAG
	    })
	else:
		return render_template('nottheflag.html')


if __name__ == '__main__':
    app.run(debug=False)
