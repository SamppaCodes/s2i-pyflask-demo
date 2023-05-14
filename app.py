from flask import Flask, jsonify
from flask_oidc import OpenIDConnect

app = Flask(__name__)

# Configure the OpenIDConnect extension
app.config['OIDC_CLIENT_SECRETS'] = 'client_secrets.json'
app.config['OIDC_COOKIE_SECURE'] = False
app.config['OIDC_SCOPES'] = ['openid', 'email', 'profile']
oidc = OpenIDConnect(app)

@app.route('/')
def hello_world():
    return '<h1>Hello, World ! - Pyflask Demo</h1>'

@app.route('/version')
def get_version():
    return '<h1>App version : <b>1.0</b></h1>'

@app.route('/test')
def get_test():
    return '<h1>You are accessing /test endpoint</h1>'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
