#from streamlit_webrtc import webrtc_streamer, RTCConfiguration
#import av
import cv2


from io import StringIO
from pathlib import Path
import streamlit as st
import time
import os
import sys
import argparse
from PIL import Image


from io import BytesIO
import base64
#from rembg import remove

################################################### Apply Filters#############################
from PIL import Image, ImageFilter            ######## IMPORT MODULE

col1, col2, col3 = st.columns(3)

st.title('Apply Filters to Image')

st.sidebar.write("## Upload and download :gear:")

source = ("CONTOUR FILTER", "SMOOTH MORE FILTER", "SHARPEN FILTER", "EDGE ENHANCE MORE FILTER", " DETAIL FILTER", "EMBOSS FILTER","BLUR FILTER", "ALL")
source_index = st.sidebar.selectbox("Select Filter", range(
        len(source)), format_func=lambda x: source[x])


############################### Download Fuction ################################################
def convert_image(img):
    buf = BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    return byte_im


################################# Uploading image ##################################################
uploaded_file = st.sidebar.file_uploader("Upload Picture", type=['png', 'jpeg', 'jpg'])
if uploaded_file is not None:
            with st.spinner(text='Loading...'):
                 st.sidebar.image(uploaded_file)
                 st.sidebar.success("Uploaded sucessfully")
                 picture = Image.open(uploaded_file)

################################# CONTOUR FILTER ##################################################
if source_index == 0:
        if uploaded_file is not None:
                 #st.caption("<p style='color:red'>ORIGINAL IMAGE</p>")
                 st.image(uploaded_file)
                 st.caption("<p style='color:red'>CONTOUR FILTER</p>")
                 img1 = picture.filter(ImageFilter.CONTOUR)
                 st.image(img1)
                 st.sidebar.markdown("\n")
                 st.sidebar.download_button("Download Result Image", convert_image(img1), "Result.png", "image/png")       

################################# SMOOTH MORE FILTER ##################################################
if source_index == 1:
        if uploaded_file is not None:
                 st.caption("<p style='color:red'>ORIGINAL IMAGE</p>")
                 st.image(uploaded_file)
                 st.caption("<p style='color:red'>SMOOTH MORE FILTER</p>")
                 img2 = picture.filter(ImageFilter.SMOOTH_MORE)
                 st.image(img2)
                 st.sidebar.markdown("\n")
                 st.sidebar.download_button("Download Result Image", convert_image(img2), "Result.png", "image/png")

################################# SHARPEN FILTER ##################################################
if source_index == 2:
        if uploaded_file is not None:
                 st.caption("**:red[ORIGINAL IMAGE.]** ")
                 st.image(uploaded_file)
                 st.caption("**:blue[SHARPEN FILTER.]** ")
                 img3 = picture.filter(ImageFilter.SHARPEN)
                 st.image(img3)
                 st.sidebar.markdown("\n")
                 st.sidebar.download_button("Download Result Image", convert_image(img3), "Result.png", "image/png")

################################# EDGE ENHANCE MORE FILTER #########################################
if source_index == 3:
        if uploaded_file is not None:
                 st.caption("**:red[THIS IS ORIGINAL IMAGE.]** ")
                 st.image(uploaded_file)
                 st.caption("**:red[This IS EDGE ENHANCE MORE FILTER.]** ")
                 img4 = picture.filter(ImageFilter.EDGE_ENHANCE_MORE)
                 st.image(img4)
                 st.sidebar.markdown("\n")
                 st.sidebar.download_button("Download Result Image", convert_image(img4), "Result.png", "image/png")       

################################# DETAIL FILTER ##################################################
if source_index == 4:
        if uploaded_file is not None:
                 st.caption("**:red[THIS IS ORIGINAL IMAGE.]** ")
                 st.image(uploaded_file)
                 st.caption("**:red[This IS DETAIL FILTER.]** ")
                 img5 = picture.filter(ImageFilter.DETAIL)
                 st.image(img5)
                 st.sidebar.markdown("\n")
                 st.sidebar.download_button("Download Result Image", convert_image(img5), "Result.png", "image/png")       

################################# EMBOSS FILTER ##################################################
if source_index == 5:
        if uploaded_file is not None:
                 st.caption("**:red[THIS IS ORIGINAL IMAGE.]** ")
                 st.image(uploaded_file)
                 st.caption("**:red[This IS EMBOSS FILTER.]** ")
                 img6 = picture.filter(ImageFilter.EMBOSS)
                 st.image(img6)
                 st.sidebar.markdown("\n")
                 st.sidebar.download_button("Download Result Image", convert_image(img6), "Result.png", "image/png")       


################################# EMBOSS FILTER ##################################################
if source_index == 6:
        if uploaded_file is not None:
                 st.caption("**:red[THIS IS ORIGINAL IMAGE.]** ")
                 st.image(uploaded_file)
                 st.caption("**:red[This IS BLUR FILTER.]** ")
                 img7 = picture.filter(ImageFilter.GaussianBlur(radius=2))
                 st.image(img7)
                 st.sidebar.markdown("\n")
                 st.sidebar.download_button("Download Result Image", convert_image(img7), "Result.png", "image/png")       

################################# ALL FILTERS ##################################################

if source_index == 7:
        if uploaded_file is not None:
                 #st.balloons()
                 col1.caption("**:red[ORIGINAL IMAGE]**")
                 col1.image(uploaded_file)
                 col1.download_button("Download Result", convert_image(picture), "Result.png", "image/png")

                 col1.caption("**:blue[CONTOUR FILTER]** ")
                 img1 = picture.filter(ImageFilter.CONTOUR)
                 col1.image(img1)
                 col1.download_button("Download Result", convert_image(img1), "Result.png", "image/png")

                 col2.caption("**:blue[SMOOTH MORE FILTER]** ")
                 img2 = picture.filter(ImageFilter.SMOOTH_MORE)
                 col2.image(img2)
                 col2.download_button("Download Result", convert_image(img2), "Result.png", "image/png")

                 col3.caption("**:blue[SHARPEN FILTER]** ")
                 img3 = picture.filter(ImageFilter.SHARPEN)
                 col3.image(img3)
                 col3.download_button("Download Result", convert_image(img3), "Result.png", "image/png")

                 col1.caption("**:blue[EDGE ENHANCE FILTER.]** ")
                 img4 = picture.filter(ImageFilter.EDGE_ENHANCE_MORE)
                 col1.image(img4)
                 col1.download_button("Download Result", convert_image(img4), "Result.png", "image/png")

                 col2.caption("**:blue[DETAIL FILTER]**")
                 img5 = picture.filter(ImageFilter.DETAIL)
                 col2.image(img5)
                 col2.download_button("Download Result", convert_image(img5), "Result.png", "image/png")
                 
                 col3.caption("**:blue[EMBOSS FILTER]** ")
                 img6 = picture.filter(ImageFilter.EMBOSS)
                 col3.image(img6)
                 col3.download_button("Download Result", convert_image(img6), "Result.png", "image/png")

                 col2.caption("**:blue[BLUR FILTER]** ")
                 img7 = picture.filter(ImageFilter.GaussianBlur(radius=2))
                 col2.image(img7)
                 col2.download_button("Download Result", convert_image(img7), "Result.png", "image/png")

