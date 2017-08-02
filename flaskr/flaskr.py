#encoding: utf-8

from flask import Flask


app = Flask()


@app.route('/')
def index():
    return "hello world!"


if __name__ == '__main__':
    app.run(debug=True)

