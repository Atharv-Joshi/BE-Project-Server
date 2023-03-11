#api
from flask import Flask, request, Response
from gan_model import predict 
from flask_cors import CORS 
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

app = Flask(__name__)
CORS(app)

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return 'No image uploaded!', 400

    bwImage = request.files['image']
    if bwImage.filename == '':
        return 'No image selected!', 400
    else :
        file_data = bwImage.read()
        colorizedImage = predict(file_data)

    return Response(colorizedImage, mimetype='image/jpeg')

if __name__ == '__main__':
    app.run()