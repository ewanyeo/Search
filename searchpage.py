import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import random
import base64

# Clustering & Image Arguments
df = pd.read_csv("clusteredData.csv")

imageData = np.loadtxt(open("product_images.csv", "rb"), delimiter=",", skiprows=1)

cmaps = ['Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds', 'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu', 'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn']

def formatImage(image): return np.array([image[i:i+28] for i in range(0, 784, 28)])

def plotImage(idx = int, data = np.array, colour = str):
    fig, ax = plt.subplots(figsize=(10, 8))
    chosenImage = ax.imshow(formatImage(data[idx]), cmap=colour)
    ax.axis('off') # remove the axis
    return st.pyplot(fig=chosenImage.axes.figure, clear_figure=True)

# Set Background
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpeg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('image_file.jpeg')

# Products Page
def main():
    # Create a banner at the top with links to other pages
    with st.container():
        st.markdown(
            """
            <div style='background-color: white; padding: 1px;'>
            <h1 style='font-family:Optima;color: #8B4513; text-align: center;'>Jorge & Jeff</h1>
            <p style='font-family: Optima;color: #8B4513; text-align: center; font-size: 20px;'> 
            <a style='color: #8B4513; text-decoration: none;' href='https://charlotteg1224-scenarioweek-homepage-zb4jfq.streamlit.app/'target='_blank'>Home</a> | 
            <a style='color: #8B4513; text-decoration: none;' href='https://ewanyeo-search-searchpage-ga2mq2.streamlit.app/'target='_blank'>Search</a> | 
            <a style='color: #8B4513; text-decoration: none;' href='https://ewanyeo-readytowear-productspage-14irvc.streamlit.app/'target='_blank'>Ready To Wear</a> | 
            <a style='color: #8B4513; text-decoration: none;' href='https://rajatk21-sw-doggy-pe2mzu.streamlit.app/' target='_blank'>Team</a> |
            <a style='color: #8B4513; text-decoration: none;' href='https://georginapalmer-contactus-streamlitcontactus-49oqai.streamlit.app/'target='_blank'>Contact</a> 
            </p>
            </div>
            """,
            unsafe_allow_html=True
        )
if __name__ == '__main__':
     main()

# leave space
st.title("")
st.text("")

# Search Items - try and change size
choice = st.number_input('Please input product no.', min_value=0, max_value=9999)
plotImage(idx = choice, data = imageData, colour = "OrRd")

# leave space
st.title("")
st.text("")

# Show recommended items
mightlike_title = '<strong><p style="font-family:Optima; color:#8B4513; font-size: 30px;">You Might Also Like</p></strong>'
st.markdown(mightlike_title, unsafe_allow_html=True)
chosen_item = df.loc[choice, 'Segment K-means PCA']
chosen_cluster = df.loc[df['Segment K-means PCA'] == chosen_item].index.values.tolist()
for i in random.sample(cmaps, 3):
    plotImage(idx = random.choice(chosen_cluster), data = imageData, colour = i)

# leave space
st.title("")
st.text("")
