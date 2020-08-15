from flask import Flask, render_template, request, make_response, session, redirect, url_for, flash, abort
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)
app.secret_key = "randomString"

@app.errorhandler(401)
def errorPage(e):
    return render_template('error.html'), 401

@app.route('/')
def index():
    search = request.args.get('search')
    return render_template('index.html', search=search)

@app.route('/profile/<username>')
def profile(username):
    return render_template('profile.html', username=username)

@app.route('/blog/<int:blogId>')
def blog(blogId):
    return 'Kamu berada di blog nomor %s' % blogId


@app.route('/login', methods=['GET', 'POST'])
def login():
    if(request.method == 'POST'):
        # Error page
        if request.form['password'] == '':
            abort(401)

        # Cookie
        resp = make_response('Email kamu adalah ' + request.form['email'])
        resp.set_cookie('email', request.form['email'])

        # Session
        session['username'] = 'lukman'

        flash('Kamu berhasil login...', 'success')

        return redirect(url_for('profile', username=session['username']))

    if 'username' in session:
        username = session['username']
        return redirect(url_for('profile', username=username))


    return render_template('login.html')

@app.route('/getcookie')
def getCookie():
    email = request.cookies.get('email')
    return 'Email yang tersimpan di cookie adalah ' + email

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

# Upload
ALLOWED_EXTENSION = set(['png', 'jpeg', 'jpg'])
app.config['UPLOAD_FOLDER']  = 'uploads'

def allowedFile(filename):
    return '.' in filename and filename.split('.', 1)[1].lower() in ALLOWED_EXTENSION

@app.route('/upload', methods=['GET', 'POST'])
def uploadFile():
    if request.method == 'POST':

        file = request.files['file']

        if 'file' not in request.files:
            return redirect(request.url)
        
        if file.filename == '':
            return redirect(request.url)
        
        if file and allowedFile(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return 'file berhasil di upload di ' + filename

    return render_template('upload.html')

app.run(debug=True)