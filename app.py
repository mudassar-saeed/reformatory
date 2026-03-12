import os
import uuid
from io import BytesIO
from flask import Flask, render_template, request, send_file, jsonify
from config import Config
from converters.pdf_to_word import convert_pdf_to_word
from converters.word_to_pdf import convert_word_to_pdf


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

def allowed_file(filename, allowed_exts):
    """FIX: Accept a specific set of extensions per route instead of a global set."""
    return (
        "." in filename and
        filename.rsplit(".", 1)[1].lower() in allowed_exts
    )


# -------------------------------
# Routes
# -------------------------------

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/pdf_to_word", methods=["GET", "POST"])
def pdf_to_word():
    if request.method == "POST":

        if "file" not in request.files:
            # FIX: Return JSON errors so the AJAX handler can show proper messages
            return jsonify(error="No file uploaded"), 400

        file = request.files["file"]

        if file.filename == "":
            return jsonify(error="No file selected"), 400

        if not allowed_file(file.filename, {"pdf"}):
            return jsonify(error="Only PDF files are allowed"), 400

        unique_id = str(uuid.uuid4())
        input_path = os.path.join(app.config["UPLOAD_FOLDER"], f"{unique_id}.pdf")
        output_path = os.path.join(app.config["OUTPUT_FOLDER"], f"{unique_id}.docx")

        try:
            file.save(input_path)
            convert_pdf_to_word(input_path, output_path)

            with open(output_path, "rb") as f:
                file_data = BytesIO(f.read())
            file_data.seek(0)

        except Exception as e:
            return jsonify(error=str(e)), 500

        finally:
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

    return render_template("pdf_to_word.html")


@app.route("/word_to_pdf", methods=["GET", "POST"])
def word_to_pdf():
    """FIX: New route — was completely missing."""
    if request.method == "POST":

        if "file" not in request.files:
            return jsonify(error="No file uploaded"), 400

        file = request.files["file"]

        if file.filename == "":
            return jsonify(error="No file selected"), 400

        if not allowed_file(file.filename, {"docx", "doc"}):
            return jsonify(error="Only Word (.docx) files are allowed"), 400

        unique_id = str(uuid.uuid4())
        input_path = os.path.join(app.config["UPLOAD_FOLDER"], f"{unique_id}.docx")
        output_path = os.path.join(app.config["OUTPUT_FOLDER"], f"{unique_id}.pdf")

        try:
            file.save(input_path)
            convert_word_to_pdf(input_path, output_path)

            with open(output_path, "rb") as f:
                file_data = BytesIO(f.read())
            file_data.seek(0)

        except Exception as e:
            return jsonify(error=str(e)), 500

        finally:
            if os.path.exists(input_path):
                os.remove(input_path)
            if os.path.exists(output_path):
                os.remove(output_path)

        return send_file(
            file_data,
            as_attachment=True,
            download_name="converted.pdf",
            mimetype="application/pdf"
        )

    return render_template("word_to_pdf.html")


# -------------------------------
# Error Handlers
# -------------------------------

@app.errorhandler(413)
def file_too_large(e):
    return jsonify(error="File is too large. Maximum allowed size is 10MB."), 413


# -------------------------------
# Run App
# -------------------------------

if __name__ == "__main__":
    app.run(debug=True)
