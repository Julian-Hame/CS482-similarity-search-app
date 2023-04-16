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
