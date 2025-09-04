import streamlit as st
from PIL import Image

st.title("v0.1")


if st.button("Show v0.1"):
    image = Image.open("v0.png")
    st.image(image, caption="Here it is!")
    st.write("Yea this unfinished")