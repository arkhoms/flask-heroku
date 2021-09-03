from flask import Flask, jsonify
#from flask import Flask, render_template
from flask import Flask, request, redirect, url_for, render_template, send_from_directory,flash 
#from werkzeug.utils import secure_filename
import cv2
#import numpy as np

app = Flask(__name__)

data = [
        {
            "id": 1,
            "library": "Pandas",
            "language": "Python"
        },
        {
            "id": 2,
            "library": "requests",
            "language": "Python"
        },
        {
            "id": 3,
            "library": "NumPy",
            "language": "Python"
        }
    ]

'''@app.route('/')
def hello():
    return "Hello Flask-Herok" '''

UPLOAD_FOLDER ='static/uploads/'
DOWNLOAD_FOLDER = 'static/downloads/'
ALLOWED_EXTENSIONS = {'jpg', 'png','.jpeg'}
app = Flask(__name__, static_url_path="/static")
# APP CONFIGURATIONS
app.config['SECRET_KEY'] = 'opencv'  
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
# limit upload size upto 6mb
app.config['MAX_CONTENT_LENGTH'] = 6 * 1024 * 1024
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


#@app.route('/', methods=['GET', 'POST'])
@app.route('/')
def index():
#    if request.method == 'POST':
#        if 'file' not in request.files:
#            flash('No file attached in request')
#            return redirect(request.url)
#        file = request.files['file']
#        if file.filename == '':
#            flash('No file selected')
#            return redirect(request.url)
#        if file and allowed_file(file.filename):
#            filename = secure_filename(file.filename)
#            file.save(os.path.join(UPLOAD_FOLDER, filename))
#            process_file(os.path.join(UPLOAD_FOLDER, filename), filename)
#            data={
#                "processed_img":'static/downloads/'+filename,
#                "uploaded_img":'static/uploads/'+filename
#            }
#            return render_template("index.html",data=data)  
#    return render_template('index.html')
    return "test"


@app.route('/api', methods=['GET'])
def get_api():
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=False)
