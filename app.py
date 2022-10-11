import streamlit as st
import os
import pandas as pd
import docx2txt
from PIL import Image 
from PyPDF2 import PdfFileReader
import pdfplumber

st.write("""
  # Resume Analyser
  Hello World!
""")


def read_pdf(file):
	pdfReader = PdfFileReader(file)
	count = pdfReader.numPages
	all_page_text = ""
	for i in range(count):
		page = pdfReader.getPage(i)
		all_page_text += page.extractText()

	return all_page_text

uploaded_files = st.file_uploader("Choose a file", type=["pdf","docx","txt"])
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

if st.button("Process"):
    if uploaded_files is not None:
        file_details={"filename":uploaded_files.name,
        "filetype":uploaded_files.type,"filesize":uploaded_files.size}
        st.write(file_details)
        with open(os.path.join(os.getcwd(),uploaded_files.name),"wb") as f: 
            f.write(uploaded_files.getbuffer())
        st.write("Success Saved")

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

