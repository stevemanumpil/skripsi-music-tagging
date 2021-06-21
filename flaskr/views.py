from flask import (Blueprint, render_template, request, current_app)
from werkzeug.utils import secure_filename
from .audio_processing import (segment_audio, compute_melgram)
from .model import audio_predict
import json

import os

views = Blueprint('views', __name__)

ALLOWED_FILE = ['mp3']

@views.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@views.route('/predict', methods=["POST"])
def predict_song():
    file = request.files['lagu']
    ext = file.filename.split('.')[-1]
    name = '.'.join(file.filename.split('.')[:-1])
    if ext in ALLOWED_FILE:
        filename_save = secure_filename(file.filename)
        path = os.path.join(current_app.config["UPLOAD_FOLDER"],filename_save)
        file.save(path)
        
        audio_segments = segment_audio(path)
        melgram_segments = compute_melgram(audio_segments)
        result = audio_predict(melgram_segments, name)

        os.remove(path)
        return json.dumps({'result': 'success','data': result})
    else:
        return json.dumps({'result','failed'})
    