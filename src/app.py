import os
from flask import Flask, render_template, request

app = Flask(__name__)


APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route("/")
def index():
    return render_template("upload.html")


@app.route("/upload", methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'DirForUploadedFiles/')
    print(target)

    if not os.path.isdir(target):
        os.mkdir(target)

    for file in request.files.getlist("file"):
        print(file)
        filename = file.filename
        if filename[-4:] == '.pdf':
            destination = "/".join([target, filename])
            print(destination)
            file.save(destination)
            return render_template("complete.html")
        elif filename[-4:] == '.doc':
            destination = "/".join([target, filename])
            print(destination)
            file.save(destination)
            return render_template("complete.html")
        elif filename[-5:] == '.docx':
            destination = "/".join([target, filename])
            print(destination)
            file.save(destination)
            return render_template("complete.html")
        else:
            return render_template("invalid.html")


if __name__ == "__main__":
    app.run(port=4555, debug=True)

