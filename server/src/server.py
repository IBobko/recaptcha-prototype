from flask import Flask, render_template, request, send_from_directory
import requests, json


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/case1',methods=["GET", "POST"])
def case1():
    if request.method == "POST":
        return get_validation("6Lep2aUZAAAAANyd7If3D-zVLq6Jjmbn9IXelS1b")
    return render_template('case1.html')


@app.route('/case2',methods=["GET", "POST"])
def case2():
    if request.method == "POST":
        return get_validation("6Lc93KUZAAAAAILSS0gkw812rhbgenBuYUZ5Zek5")
    return render_template('case2.html')


@app.route('/case3',methods=["GET", "POST"])
def case3():
    if request.method == "POST":
        return get_validation("6LfF3KUZAAAAAP9fv2mWt--khuAbjH7HV___nmTv")
    return render_template('case3.html')


def get_validation(secret_key):
    data = {
        "secret": secret_key,
        "response": request.form['g-recaptcha-response']
    }
    response = requests.post("https://www.google.com/recaptcha/api/siteverify", data=data)
    return json.loads(response.text)


@app.route("/static/<path:path>")
def static_dir(path):
    return send_from_directory("static", path)


if __name__ == '__main__':
    app.run('0.0.0.0', 5000)
    #app.run(ssl_context='adhoc')
