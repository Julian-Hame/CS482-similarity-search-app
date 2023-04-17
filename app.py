import streamlit as st
from transformers import pipeline
import pickle
from PIL import Image

st.title('Similar Faces Searcher')
filenames = []
filenames = pickle.load(open('filenames.pickle', 'rb'))
feature_dict = pickle.load(open('feature_dict.pickle', 'rb'))

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
    query_image = st.number_input('Enter the ID number of the dataset image you would like to use.', value = 1, max_value = 232
                                 min_value = 0, value = 0)
    st.write('You selected:', image_names[query_image])
    st.write("Person: " +person_names[query_image])

with col2:
    file_name = st.file_uploader("Upload your own image")
st.write("---")

# Display query image
st.write("Your Image")
st.write("Filename: " +image_names[query_image])
st.write("Person: " +person_names[query_image])
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#plt.imshow(mpimg.imread(filenames[query_image]))

# Turn feature vectors of dictionary into a 2D list that can be fed into NN algorithm
feature_list = list(feature_dict.values())

x = 0
while x < len(feature_list):
  feature_list[x] = list(feature_list[x])
  x = x + 1

# Nearest Neighbor Algorithm
from sklearn.neighbors import NearestNeighbors

neighbors = NearestNeighbors(n_neighbors=11, algorithm='brute',
metric='euclidean').fit(feature_list)
distances, indices = neighbors.kneighbors([feature_list[query_image]])

# Display most similar image
st.write("----------------------------------------")
st.write("Most Similar:")
st.write("Person:   " +person_names[list(indices[0])[1]])
st.write("Filename: " +image_names[list(indices[0])[1]])
#plt.imshow(mpimg.imread(filenames[list(indices[0])[1]]))

# Display second most similar image
st.write("----------------------------------------")
st.write("2nd Most Similar:")
st.write("Person:   " +person_names[list(indices[0])[2]])
st.write("Filename: " +image_names[list(indices[0])[2]])
#plt.imshow(mpimg.imread(filenames[list(indices[0])[2]]))

# Display third most similar image
st.write("----------------------------------------")
st.write("3rd Most Similar:")
st.write("Person:   " +person_names[list(indices[0])[3]])
st.write("Filename: " +image_names[list(indices[0])[3]])
#plt.imshow(mpimg.imread(filenames[list(indices[0])[3]]))

# Display fourth most similar image
st.write("----------------------------------------")
st.write("4th Most Similar:")
st.write("Person:   " +person_names[list(indices[0])[4]])
st.write("Filename: " +image_names[list(indices[0])[4]])
#plt.imshow(mpimg.imread(filenames[list(indices[0])[4]]))

# Display fifth most similar image
st.write("----------------------------------------")
st.write("5th Most Similar:")
st.write("Person:   " +person_names[list(indices[0])[5]])
st.write("Filename: " +image_names[list(indices[0])[5]])
#plt.imshow(mpimg.imread(filenames[list(indices[0])[5]]))

# Display sixth most similar image
st.write("----------------------------------------")
st.write("6th Most Similar:")
st.write("Person:   " +person_names[list(indices[0])[6]])
st.write("Filename: " +image_names[list(indices[0])[6]])
#plt.imshow(mpimg.imread(filenames[list(indices[0])[6]]))

# Display seventh most similar image
st.write("----------------------------------------")
st.write("7th Most Similar:")
st.write("Person:   " +person_names[list(indices[0])[7]])
st.write("Filename: " +image_names[list(indices[0])[7]])
#plt.imshow(mpimg.imread(filenames[list(indices[0])[7]]))

# Display eigth most similar image
st.write("----------------------------------------")
st.write("8th Most Similar:")
st.write("Person:   " +person_names[list(indices[0])[8]])
st.write("Filename: " +image_names[list(indices[0])[8]])
#plt.imshow(mpimg.imread(filenames[list(indices[0])[8]]))

# Display ninth most similar image
st.write("----------------------------------------")
st.write("9th Most Similar:")
st.write("Person:   " +person_names[list(indices[0])[9]])
st.write("Filename: " +image_names[list(indices[0])[9]])
#plt.imshow(mpimg.imread(filenames[list(indices[0])[9]]))

# Display tenth most similar image
st.write("----------------------------------------")
st.write("10th Most Similar:")
st.write("Person:   " +person_names[list(indices[0])[10]])
st.write("Filename: " +image_names[list(indices[0])[10]])
#plt.imshow(mpimg.imread(filenames[list(indices[0])[10]]))
