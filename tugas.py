from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"
    
@app.route('/about')
def about():
    return render_template('index.html')

@app.route('/nama/<string:nama>')
def getnama(nama):
    return "nama saya ialaah {}".format(nama)

@app.route('/user/<int:user_id>')  
def user_id(user_id):
    return f"ID saya : {user_id}"


from flask import Flask

app = Flask(__name__)

@app.route('/user/<name>')  
def user(name):
    return f"perkenalkan nama saya, {name}!"


if __name__ == '__main__':
    app.run(debug=True)

if __name__ == "__main__":
    app.run(debug=False)


