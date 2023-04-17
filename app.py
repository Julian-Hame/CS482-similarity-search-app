import streamlit as st
from transformers import pipeline
import pickle
from PIL import Image

st.title('Similar Faces Searcher')
filenames = []
filenames = pickle.load(open('filenames.pickle', 'rb'))

person_names = []
image_names = []
x = 0
while x < len(filenames):
  split_name = filenames[x].split('/')
  person_names.append(split_name[4].replace("_", " "))
  image_names.append(split_name[5])
  x = x + 1
    
st.write("---")
st.header('Select or upload an image')
col1, col2 = st.columns(2)
selection = "N/A"

with col1:
    query_image = st.number_input('Enter the ID number of the dataset image you would like to use.', value = 1)
    st.write('You selected:', image_names[query_image])

with col2:
    file_name = st.file_uploader("Upload your own image")
st.write("---")

# Display query image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
%matplotlib inline

st.write("Person:   " +person_names[query_image])
st.write("Filename: " +image_names[query_image])
plt.imshow(mpimg.imread(filenames[query_image]))
