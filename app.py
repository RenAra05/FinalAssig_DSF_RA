import streamlit as st
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.models import Sequential

st.set_option('deprecation.showfileUploaderEncoding',False)
st.cache(allow_output_mutation=True)
def load_model():
  model = tf.keras.models.load_model('/home/admusr/FinPro_DSF/flower_identification.h5')
  return model
model = load_model()
st.write("""
         # Flower Classification
         """
         )

file=st.file_uploader("Please upload an flower image('daisy','dandelion','roses','sunflowers','tulips'):", type=["jpg","png","jpeg"])
import cv2
from PIL import Image, ImageOps
import numpy as np
def import_and_predict(image_data, model):

  size = (180,180)
  image = ImageOps.fit(image_data, size, Image.ANTIALIAS)
  img = np.asarray(image)
  img_reshape = img[np.newaxis,...]
  prediction = model.predict(img_reshape)

  return prediction
if file is None:
  st.text("Please upload an image file")
else:
  image = Image.open(file)
  st.image(image, use_column_width=True)
  predictions = import_and_predict(image, model)
  class_names = ['daisy','dandelion','roses','sunflowers','tulips']
  string = "This image most likely is: "+class_names[np.argmax(predictions)]
  st.success(string)
