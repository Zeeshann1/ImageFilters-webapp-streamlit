
## Image Filters Webapp Based On Streamlit
- Apply filters to your images using streamlit based webapp program </p>
- [Demonstration](https://zeeshann1-imagefilters-webapp-streamlit-image-filters-08we9s.streamlit.app/)




## Filters

- CONTOUR FILTER
- SMOOTH MORE FILTER
- SHARPEN FILTER
- EDGE ENHANCE MORE FILTER
- DETAIL FILTER
- EMBOSS FILTER
- BLUR FILTER
- REMOVE BACKGROUND
- ALL





## Deployment

Use python 3.8.15 version. Create virtual environment using anaconda. Conda version (4.12.0).

Create Virtual Environment:

```bash
  conda create --name py38 python==3.8
  conda activate py38
  pip install -r requirements.txt
```

Requirements:

```bash
  pip install streamlit-webrtc
  pip install streamlit
  pip install opencv-python
  pip install numpy
  pip install rembg
  pip install pillow
  pip install -r requirements.txt
```

How to Run:

```bash
streamlit run Image_filters.py
```
# Results
## Remove Background
<img src="bg.png"/>

## Apply all filters at once
<img src="all.png"/>
