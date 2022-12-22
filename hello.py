from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1><i>Hello World!<i></h1>"

if __name__ == "__main__":
    app.run(host='192.168.68.128', port=9090)