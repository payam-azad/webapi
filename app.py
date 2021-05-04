from flask import Flask, jsonify, request, flash, render_template, Markup
from flask_cors import CORS

version = "0.0.1"
app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return f"start page for version {version}"


@app.route("/test", methods=['GET', 'POST'])
def hello():
    try:
        message = request.json['name']
    except Exception as e:
        message = str(e)
    return {'method': request.method,
            'request_text': str(request.json),
            'message': message}


if __name__ == '__main__':
    app.run(debug=True)
