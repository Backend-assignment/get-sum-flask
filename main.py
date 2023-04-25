from flask import Flask

app = Flask(__name__)

@app.route('/bosh')
@app.route('/')
@app.route('/home')
@app.route('/about')
@app.route('/about/me')
def me():
    return 'About me!'


if __name__ == '__main__':
    app.run(debug=True)