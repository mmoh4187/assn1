from flask import Flask, request, render_template

app = Flask(__name__)
host="localhost"
port="5000"
address="http://{0}:{1}".format(host,port)

users = {"test":"test123", "admin":"admin"}

def serve_forever():
    app.run(host, port)

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError("Not running with Werkzeug server")
    func()

@app.route('/shutdown')
def shutdown():
    shutdown_server()

@app.route('/')
def hello():
    return 'Hello World'

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db_passwd = users.get(username)
        if password == db_passwd:
            return "Success"
        else:
            return "Fail"
    else:
        return render_template("login.html")


if __name__ == '__main__':
    serve_forever()