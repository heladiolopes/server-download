import os
from flask import Flask, abort, send_file

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/download/<filename>')
def download(filename):

    file = os.getcwd() + '/file-base/' + filename

    if os.path.isfile(file):
        return send_file(file, as_attachment=True)
    else:
        abort(404)


if __name__ == '__main__':
    app.run(debug=True)
