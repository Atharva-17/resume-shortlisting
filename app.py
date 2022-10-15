from turtle import width
import streamlit as st
import os
import pandas as pd
#import docx2txt
from PIL import Image 
from PyPDF2 import PdfFileReader
#import pdfplumber
import FILETOIMAGE.pdftoimage as ftoimage
import OCR.ocr as ocr
import PLOTBOX.plotbox as plot
import RESUMEANALYSIS.analyze  as analysis
import cv2
st.set_page_config(layout="wide")
st.write("""
  # Resume Analyser
""")
skills_panel , resume_panel = st.columns(2)
skills_panel.header("Skills")
resume_panel.header("Resume")



def read_pdf(file):
	pdfReader = PdfFileReader(file)
	count = pdfReader.numPages
	all_page_text = ""
	for i in range(count):
		page = pdfReader.getPage(i)
		all_page_text += page.extractText()

	return all_page_text

uploaded_files = resume_panel.file_uploader("Choose a file", type=["pdf","docx","txt"] , accept_multiple_files=True)
uploaded_skills_files = skills_panel.file_uploader("Choose a file", type=["csv"] , accept_multiple_files=False)
# for uploaded_file in uploaded_files:
#     bytes_data = uploaded_file.read()
#     st.write("filename:", uploaded_file.name)
#     st.write(bytes_data)

# def show_pdf(file_path):
#     with open(file_path,"rb") as f:
#         base64_pdf = base64.b64encode(f.read()).decode('utf-8')
#     pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="800" height="800" type="application/pdf"></iframe>'
#     st.markdown(pdf_display, unsafe_allow_html=True)

# show_pdf(uploaded_file.name)
if skills_panel.button("Process Skills"):
    if uploaded_skills_files is not None:
        skills_panel.write("Hello")
    else:
        skills_panel.warning("please upload a file")



if resume_panel.button("Process"):
    if uploaded_files is not None:
        for uploaded_file in uploaded_files:
            file_details={"filename":uploaded_file.name,
            "filetype":uploaded_file.type,"filesize":uploaded_file.size}
            #st.write(file_details)
            with open(os.path.join(os.getcwd(),uploaded_file.name),"wb") as f: 
                f.write(uploaded_file.getbuffer())
            resume_panel.write("Success Saved")
            images = ftoimage.filetoimage(uploaded_file.name)
            image = []
            for i in images:
                input = ocr.ImageToText(i)
                skills , phone = analysis.analyze(input)
                image.append( plot.plotSkills(i , input , skills) )
                resume_panel.write(skills)
                resume_panel.image(image)
            os.remove(os.path.join(os.getcwd(),uploaded_file.name))

        # if uploaded_files.type == "text/plain":
        #     # raw_text=uploaded_files.read()
        #     # st.write(raw_text)
        #     raw_text=str(uploaded_files.read(),"utf-8")
        #     st.write(raw_text)
        #     st.text(raw_text)
        # elif uploaded_files == "application/pdf":
        #     try:
        #         with pdfplumber.open(uploaded_files) as pdf:
        #             pages = pdf.pages[0]
        #             st.write(pages.extract_text())
        #     except:
        #         st.write("none")        
        #     # raw_text=read_pdf(uploaded_files)
        #     # st.write(raw_text)   
        # else:
        #     raw_text=docx2txt.process(uploaded_files)
        #     st.write(raw_text)

