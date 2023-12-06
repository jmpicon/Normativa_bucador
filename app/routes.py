from flask import render_template
from werkzeug.urls import url_quote


@app.route('/')
def index():
    return render_template('index.html')
