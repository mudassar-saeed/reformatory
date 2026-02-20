import os
import uuid
from io import BytesIO
from flask import Flask, render_template, request, send_file, redirect, flash
from config import Config
from converter.converter import convert_pdf_to_word


# -------------------------------
# App Initialization
# -------------------------------

app = Flask(__name__)
app.config.from_object(Config)

# Ensure required folders exist
os.makedirs(app.config["UPLOAD_FOLDER"], exist_ok=True)
os.makedirs(app.config["OUTPUT_FOLDER"], exist_ok=True)


# -------------------------------
# Helper Functions
# -------------------------------

def allowed_file(filename):
    return (
        "." in filename and
        filename.rsplit(".", 1)[1].lower() in app.config["ALLOWED_EXTENSIONS"]
    )


# -------------------------------
# Routes
# -------------------------------

@app.route("/", methods=["GET", "POST"])
def convert():
    if request.method == "POST":

        if "file" not in request.files:
            return "No file uploaded", 400

        file = request.files["file"]

        if file.filename == "":
            return "No file selected", 400

        if not allowed_file(file.filename):
            return "Only PDF files are allowed", 400

        # Generate unique filenames
        unique_id = str(uuid.uuid4())
        input_path = os.path.join(app.config["UPLOAD_FOLDER"], f"{unique_id}.pdf")
        output_path = os.path.join(app.config["OUTPUT_FOLDER"], f"{unique_id}.docx")

        try:
            # Save uploaded file
            file.save(input_path)

            # Convert PDF to Word
            convert_pdf_to_word(input_path, output_path)

            # Read converted file into memory
            with open(output_path, "rb") as f:
                file_data = BytesIO(f.read())

            file_data.seek(0)

        finally:
            # Cleanup files safely
            if os.path.exists(input_path):
                os.remove(input_path)

            if os.path.exists(output_path):
                os.remove(output_path)

        return send_file(
            file_data,
            as_attachment=True,
            download_name="converted.docx",
            mimetype="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )

    return render_template("index.html")


# -------------------------------
# Error Handlers
# -------------------------------

@app.errorhandler(413)
def file_too_large(e):
    return "File is too large. Maximum allowed size is 10MB.", 413


# -------------------------------
# Run App
# -------------------------------

if __name__ == "__main__":
    app.run(debug=True)
