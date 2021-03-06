from flask import Flask, flash, redirect, render_template, request,session, abort
from flask_cors import CORS
import os
app = Flask(__name__)

cors = CORS(app, resource={r"/*":{"origins": "*"}})

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

#@app.route("/deploy", methods=['GET'])    
#def deploy():
    #return "<h1>Testando deploy GitHub x Heroku </h1>"

def main():
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

if __name__ == "__main__":
    main()