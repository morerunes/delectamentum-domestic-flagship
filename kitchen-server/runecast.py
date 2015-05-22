from flask import Flask, request
import uuid

app = Flask(__name__)

queue = []

@app.route('/')
def list_current():
	return 'Welcome to the Rune Cast!'

@app.route('/append', method='POST')
def append():
	track = {}
	trackID = uuid4()
	
	track['title'] = request.form['title']
	track['location'] = request.form['location']
	track['protocol'] = derive_protocol(request.form['location'])

def derive_protocol(location):
	return 'local' # TODO

if __name__ == '__main__':
	app.run(debug=True)
