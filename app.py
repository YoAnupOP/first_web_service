from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return '<h1>YO!</h1><p>I m Anup</p>'

@app.route('/api/status')
def status():
    return {'status' :'operational', 'owner':'Anup'}

if __name__ == '__main__':
    app.run(debug=True)