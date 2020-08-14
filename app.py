from flask import Flask, render_template, request
app = Flask(__name__)

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
        return 'Email kamu adalah ' + request.form['email']

    return render_template('login.html')


app.run(debug=True)