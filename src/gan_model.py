from PIL import Image
import numpy as np
from matplotlib import image
from matplotlib import pyplot as plt
import os
import io
from tensorflow.keras.models import load_model

model = load_model("model/i20_e1000.h5")
model.compile(loss="binary_crossentropy", optimizer="adam", metrics = ['accuracy'])

img_size = 120

def predict(bwImage):
  x = []
  y = []
  rgb_image = Image.open(io.BytesIO(bwImage)).resize( ( img_size , img_size ) )

  rgb_img_array = (np.asarray( rgb_image ) ) / 255
  gray_image = rgb_image.convert( 'L' )

  gray_img_array = ( np.asarray( gray_image ).reshape( ( img_size , img_size , 1 ) ) ) / 255

  x.append( gray_img_array )

  inputData = np.array(x)

  y = model( inputData[0 : ] ).numpy()

  for i in range(len(inputData)):
    colorizedImage = Image.fromarray( ( y[i] * 255 ).astype( 'uint8' ) ).resize( ( 1024 , 1024 ) )

    jpeg_image = io.BytesIO()
    colorizedImage.save(jpeg_image, 'JPEG')
    jpeg_image.seek(0)

  return jpeg_image