from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' %username

@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'Post %d' %post_id

@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if vaild_login(request.form['username'],
                       request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invaild username or password'
    return render_template('login.html', error = error)

if __name__== '__main__':
    app.run(host='0.0.0.0',debug=True)
