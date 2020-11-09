import os
import cv2
import glob
import sys
from os.path import isfile, join
from flask import Flask, flash, request, redirect, render_template, json
from werkzeug.utils import secure_filename

app=Flask(__name__)
app.secret_key = "secret key" # for encrypting the session

#It will allow below 16MB contents only, you can change it
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

path = os.getcwd()
# file Upload
UPLOAD_FOLDER = os.path.join(path, 'uploads')
# Make directory if "uploads" folder not exists
if not os.path.isdir(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
ALLOWED_EXTENSIONS = set(['jpg'])

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def upload_form():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def upload_file():
    if request.method == 'POST':

        if 'files[]' not in request.files:
            flash('No file part')
            return redirect(request.url)

        files = request.files.getlist('files[]')

        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

        flash('Archivo(s) cargados correctamente')
        return redirect('/process')

@app.route('/process')
def process_images():
    images_files = "uploads"
    
    content = os.listdir(images_files)

    images = []

    for file in content:
        if os.path.isfile(os.path.join(images_files, file)):
            images.append(file)
    
    for img in range(0, len(images)):
        images[img] = cv2.imread(join(images_files,images[img]))
        print(img, file=sys.stderr)
    
    return images


if __name__ == "__main__":
    app.run(host='127.0.0.1',port=5000,debug=False,threaded=True)
