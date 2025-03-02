from flask import Flask, render_template, request, send_file
import os
from werkzeug.utils import secure_filename
from image_processor import process_image
from document_generator import create_doc
from email_sender import send_email

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['OUTPUT_FOLDER'] = 'outputs'
DEFAULT_EMAIL = "amrs.tech@gmail.com"

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    if 'image' not in request.files:
        return "No file part", 400
    file = request.files['image']
    if file.filename == '':
        return "No selected file", 400
    
    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
    
    extracted_text = process_image(filepath)
    
    doc_path = os.path.join(app.config['OUTPUT_FOLDER'], f"{os.path.splitext(filename)[0]}.docx")
    create_doc(extracted_text, doc_path)
    
    send_email(DEFAULT_EMAIL, doc_path)
    
    return send_file(doc_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
