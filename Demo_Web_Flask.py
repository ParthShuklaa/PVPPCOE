from flask import Flask

app = Flask(__name__)

@app.route("/")
def Hello_World():
    return "<h1>hello Word</h1>"
@app.route("/SignUp")
def Signup():
    return "<h2><b>Welcome to signup page ...!!!!!</b></h2>"

if __name__ == '__main__':
    app.run()

