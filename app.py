from flask import Flask, render_template, request, make_response, session, redirect, url_for, flash
app = Flask(__name__)
app.secret_key = "randomString"

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

app.run(debug=True)