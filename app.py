from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Halaman index'

@app.route('/setting')
def setting():
    return 'Halaman setting'

@app.route('/profile/<username>')
def profile(username):
    return 'Halo kamu berada dihalaman profil %s' % username

@app.route('/blog/<int:blogId>')
def blog(blogId):
    return 'Kamu berada di blog nomor %s' % blogId

app.run(debug=True)