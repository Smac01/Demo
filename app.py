
"""
	
	A Demo Webpage

	This webpage is just a demo page and to test azure deployment.

"""


from flask import (
	Flask,
	render_template,
	request,
	url_for,
	redirect,
	jsonify
)

app = Flask(__name__)

users = {
	'admin' : 'password123', 
	'abc' : 'password123'
}

@app.route('/')
def home():
	return render_template("index.html")

@app.route('/login')
def login():
	return render_template('login.html');

@app.route('/validate', methods=["POST"])
def validate():
	data = request.get_json();
	if(data['type'] == 'username' and data['username'] in users.keys()):
		return jsonify({
			'status': True
		})
	elif(data['type'] == 'password'and users[data['username']] == data['password'] ):
		return jsonify({
			'status': True
		})
	else:
		return jsonify({
			'status': False
		})

@app.route('/success')
def success():
	return "Login successfull"


if __name__ == '__main__':
	app.run(debug=True);