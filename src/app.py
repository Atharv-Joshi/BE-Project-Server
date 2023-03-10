#api
from flask import Flask, request, Response
from gan_model import predict 

app = Flask(__name__)

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
    app.run(debug=True)