from flask import Flask
from main import main

app = Flask(__name__)
app.register_blueprint(main, url_prefix = "")

if __name__ == '__main__':
    app.run(debug = False, host = '0.0.0.0', port = 5000)#remove debug before deployment