from flask import Flask, redirect, url_for, render_template,request
import statistics

app = Flask(__name__)

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/results/<int:score>')
def results(score):
    if score >=50:
        res = "PASS"
    else:
        res = "FAIL"
    return render_template('result.html',result = res)

@app.route('/submit', methods=['POST', 'GET'])
def submit():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        computer_science = float(request.form['compsci'])
        data_science = float(request.form['datascience'])

        score_list = [science, maths, computer_science, data_science]
        total_score = statistics.mean(score_list)

        res = ''
        return redirect(url_for('results', score=total_score))

if __name__ == '__main__':
	app.run(debug=True)