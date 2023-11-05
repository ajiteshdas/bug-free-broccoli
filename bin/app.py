from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
	return 'Hello, Flask! Welcome'

@app.route('/results/<int:score>')
def results(score):
    result = ''
    if score <=50:
        result = 'fail'
    else:
        result = 'success'
    
    return result

if __name__ == '__main__':
	app.run(debug=True)