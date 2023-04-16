# Retrieve data from pickle file
import pickle
# feature_dict = pickle.load(open('feature_dict.pickle', 'rb'))
filenames = pickle.load(open('filenames.pickle', 'wb')

# Turn image locations into actual person and image names
person_names = []
image_names = []

x = 0
while x < len(filenames):
  split_name = filenames[x].split('/')
  person_names.append(split_name[4].replace("_", " "))
  image_names.append(split_name[5])
  x = x + 1

print("Person:   " +person_names[0])
print("Filename: " +image_names[218])

'''
import streamlit as st
from transformers import pipeline
from PIL import Image

st.title('Similar Image Finder')

st.write("---")
st.header('Select or upload an image')
col1, col2 = st.columns(2)

selection = "N/A"
with col1:
    option = st.selectbox(
    'Pick an image',
    ('pic1', 'pic2', 'pic3'))

st.write('You selected:', option)

with col2:
    file_name = st.file_uploader("Upload your own image")

st.write("---")
'''
