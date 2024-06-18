import os
os.chdir(r"D:\myenv\streamlit")


import xml.etree.ElementTree as ET

# tree = ET.parse('769952.xml')
# root = tree.getroot()

# root = ET.tostring(root,encoding='utf8')
# root

def parse_xml(file):
    tree = ET.parse(file)
    root = tree.getroot()
    return ET.tostring(root, encoding='utf8')


import re,string,unicodedata
import nltk
from bs4 import BeautifulSoup

def strip_html(text):
    soup = BeautifulSoup(text,'html.parser')
    return soup.get_text()

def remove_between_square_brackets(text):
    return re.sub('\[[^]]*\]', '', text)

def denoise_text(text):
    text = strip_html(text)
    text = remove_between_square_brackets(text)
    text=re.sub('  ','',text)
    return text

# sample = denoise_text(root)


#making frontend for the application
import streamlit as st
st.title("XML Text Extractor")

#file uploader
uploaded_file = st.file_uploader("Upload XML file here",type='xml')

if uploaded_file is not None:
    raw_xml = parse_xml(uploaded_file)
    raw_text = raw_xml.decode('utf-8')
    denoised_text = denoise_text(raw_text)

     # Display the extracted and cleaned text
    st.subheader('Extracted Text')
    st.text_area("Text", denoised_text, height=300)
