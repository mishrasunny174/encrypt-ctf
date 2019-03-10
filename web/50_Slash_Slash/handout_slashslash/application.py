import os
from flask import Flask, render_template, jsonify

app = Flask(__name__)

'''
 secret_key using python3 secrets module
'''
app.secret_key = "9d367b3ba8e8654c6433379763e80c6e"

'''
Learn about virtualenv here:
https://www.youtube.com/watch?v=N5vscPTWKOk&list=PL-osiE80TeTt66h8cVpmbayBKlMTuS55y&index=7
'''

FLAG = os.getenv("FLAG", "encryptCTF{}")

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/encryptCTF', methods=["GET"])
def getflag():
	    return jsonify({
	        'flag': FLAG
	    })
	
if __name__ == '__main__':
    app.run(debug=False)