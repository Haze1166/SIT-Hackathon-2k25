from flask import Flask, request, jsonify
from flask_cors import CORS  # For handling cross-origin requests
import pdfplumber
import docx
import os

app = Flask(__name__)
# CORS(app)  # Enable CORS for all domains (BAD practice, allows any webpage to hit the service)
CORS(app, resources={r"/*": {"origins": "*"}})  # Use a more narrow setting (localhost for testing)


# --- Document Processing Functions (from previous responses) ---
def extract_text_from_pdf(file_path):
    text = ""
    try:
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"
        return text
    except Exception as e:
        print(f"Error extracting from PDF: {e}")
        return ""


def extract_text_from_docx(file_path):
    text = ""
    try:
        doc = docx.Document(file_path)
        text = "\n".join([para.text for para in doc.paragraphs])
        return text
    except Exception as e:
        print(f"Error extracting from DOCX: {e}")
        return ""


def extract_text_from_txt(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        print(f"Error extracting from TXT: {e}")
        return ""


def summarize_text(text, api_key):
    """Generates a summary using Gemini API. Replace with your actual implementation."""
    # *** REPLACE THIS WITH YOUR GEMINI API CODE ***
    #  Remember to use the api_key passed from the frontend
    print("Summarization not implemented. Returning placeholder summary.")
    return "Placeholder summary.  Integrate with Google Gemini API or another summarization method."


@app.route('/summarize', methods=['POST'])
def summarize():
    api_key = request.form['apiKey']
    filename = request.form['filename']
    file_content = request.form['fileContent']

    # Determine file type and extract text
    if filename.endswith(".pdf"):
        text = extract_text_from_pdf(file_content)  # file_content is actually the path
    elif filename.endswith(".docx"):
        text = extract_text_from_docx(file_content)
    elif filename.endswith(".txt"):
        text = extract_text_from_txt(file_content)
    else:
        return jsonify({'summary': "Unsupported file format!"})

    if text:
        summary = summarize_text(text, api_key)
        return jsonify({'summary': summary})
    else:
        return jsonify({'summary': "No text could be extracted."})


if ___name___ == '___main___':
    app.run(debug=True, port=5000)  # Or another port