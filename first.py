from flask import Flask, render_template

#name the instance
app = Flask(__name__)


@app.route('/')
def index():
	return render_template('example.html')

@app.route('/home')
def home():
	return render_template('example.html', myvar ='Flask Example')

if __name__ == '__main__':
	app.run(debug=True)
