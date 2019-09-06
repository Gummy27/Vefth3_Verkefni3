from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
	return(render_template('default.html'))

@app.route("/kennitala/<kt>")
def kt(kt):
	summa = 0
	for x in kt:
		summa += int(x)

	return(render_template('kt_summa.html', kt=kt, summa=summa))