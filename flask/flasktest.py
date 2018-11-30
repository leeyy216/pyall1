from flask import render_template
from flask import Flask
from flask import request

app = Flask(__name__)
 
@app.route('/hello')
def hello():
    return '<h1>Hello World</h1>'

@app.route('/index')
def index():
    return '<h1>Welcome to the index page.</h1>'

@app.route('/index/show/')
@app.route('/index/show/<name>')
def show(name=None):
    return render_template('show.html',name=name)

@app.route('/uploadfile',methods=['GET','POST'])
def uploadfile():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/')

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'POST':
        do_the_login()
    else:
        show_the_login_form()

#url_for('static', filename = 'flaskcss.css')

if __name__ == '__main__':
    app.run(debug=True) #debug mode
