from dotenv import load_dotenv
import streamlit as st
import os
from PIL import Image
import io
import pdf2image
import base64
import fitz

import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Google API
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, pdf_content, prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([input, pdf_content, prompt])
    return response.text

def input_pdf_setup(uploaded_file):
    if uploaded_file is not None:
        # Read the PDF file
        document = fitz.open(stream=uploaded_file.read(), filetype="pdf")
        # Initialize a list to hold the text of each page
        text_parts = []

        # Iterate over the pages of the PDF to extract the text
        for page in document:
            text_parts.append(page.get_text())

        # Concatenate the list into a single string with a space in between each part
        pdf_text_content = " ".join(text_parts)
        return pdf_text_content
    else:
        raise FileNotFoundError("No file uploaded")

## Streamlit App

# Set page title and icon
st.set_page_config(page_title="Resume Expert", page_icon=":briefcase:")

# Header with title and subtitle
st.title("ATS Tracker")
st.subheader("This Application helps you in your Resume Review with help of GEMINI AI [LLM]")

# Upload file and input field
input_text = st.text_input("Job Description:")
uploaded_file = st.file_uploader("Upload your Resume (PDF)...", type=["pdf"])

# Add some padding between elements
st.write("")
st.write("")

# Display uploaded file message
if uploaded_file is not None:
    st.success("PDF Uploaded Successfully")

# Add icons to buttons
submit1 = st.button("Tell Me About the Resume :book:")
submit2 = st.button("How Can I Improve my Skills? :bulb:")
submit3 = st.button("What are the Keywords That are Missing? :mag:")
submit4 = st.button("Percentage match :bar_chart:")
submit5 = st.button("Answer My Query :question:")

# Add custom footer
st.write("---")
st.markdown("Made By [Sanidhya](https://www.linkedin.com/in/sanidhya-rajguru-522387253/)")
st.markdown("For Queries, Reach out on [LinkedIn](https://www.linkedin.com/in/sanidhya-rajguru-522387253/)")
st.markdown("*Resume Expert - Making Job Applications Easier*")

# Add some space at the bottom
st.write("")
st.write("")

# Handle button clicks
if submit1:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_text, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload a PDF file to proceed.")

elif submit2:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_text, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload a PDF file to proceed.")

elif submit3:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_text, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload a PDF file to proceed.")

elif submit4:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_text, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload a PDF file to proceed.")

elif submit5:
    if uploaded_file is not None:
        pdf_content = input_pdf_setup(uploaded_file)
        response = get_gemini_response(input_text, pdf_content, input_text)
        st.subheader("The Response is")
        st.write(response)
    else:
        st.write("Please upload a PDF file to proceed.")
