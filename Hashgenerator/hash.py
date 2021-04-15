from flask import Flask
from flask import Flask, render_template, request, redirect, url_for, flash, session, g, send_file, make_response
import re
from tempfile import NamedTemporaryFile
import os
from datetime import date, timedelta
import random
from flask_dropzone import Dropzone
import hashlib
from flask import send_from_directory 

app = Flask(__name__)
dropzone = Dropzone(app)
# SESSION
app.secret_key = 'mysecretkey11'
adminkey = 'specialkey'

@app.route('/', methods=['GET', 'POST'])
def adminprofile():

    return render_template('adminprofile.html')


@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file: 
            filename = file.filename
            with open("./file.txt", "w") as f:  
                f.write(filename)
            makehash()
            return  render_template('adminprofile.html')
            
    return render_template('adminprofile.html')



def makehash():
    file = "./file.txt"
    BLOCK_SIZE = 65536 
    file_hash = hashlib.sha256() 
    with open(file, 'rb') as f: 
        fb = f.read(BLOCK_SIZE) 
        while len(fb) > 0: 
            file_hash.update(fb) 
            fb = f.read(BLOCK_SIZE) 
            finalhash =(file_hash.hexdigest())   
            with open("./file.txt", "w") as f:  
                f.write(finalhash)
            
    return finalhash




if __name__ == '__main__':
    app.run(port=3000, debug=True)






