from flask import Flask, request, redirect, url_for
import uuid

app = Flask(__name__)

queue = []

@app.route('/')
def list_current():
	return 'Welcome to the Rune Cast!'

@app.route('/next')
def next():
	if len(queue) < 2:
		return 'No tracks queued!'
	else:
		return str(queue[1])

@app.route('/append', methods=['POST'])
def append():
	track = {}
	trackID = uuid.uuid4()
	
	track['title'] = request.form['title']
	track['location'] = request.form['location']
	track['artist'] = request.form['artist']
	
	track['protocol'] = derive_protocol(request.form['location'])
	queue.append(track)
	return redirect(url_for('next'))

def derive_protocol(location):
	return 'local' # TODO

if __name__ == '__main__':
	app.run(debug=True)
