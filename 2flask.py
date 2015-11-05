from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def main():
	return render_template("index.html")

@app.route('/contactme')
def comment():
	return render_template("contactme.html")

@app.route('/about')
def about():
	return render_template("aboutme.html")

if __name__ == "__main__":
    app.run()