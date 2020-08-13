from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Halaman index'

app.run(debug=True)