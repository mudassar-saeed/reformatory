from pdf2docx import Converter
import os


def convert_pdf_to_word(input_path: str, output_path: str) -> None:
    """
    Converts a PDF file to a Word (.docx) file.

    :param input_path: Path to the input PDF file
    :param output_path: Path where the output DOCX file will be saved
    :raises FileNotFoundError: If input file does not exist
    :raises Exception: If conversion fails
    """

    # Check if input file exists
    if not os.path.exists(input_path):
        raise FileNotFoundError(f"Input file not found: {input_path}")

    try:
        converter = Converter(input_path)
        converter.convert(output_path, start=0, end=None)
        converter.close()

    except Exception as e:
        raise Exception(f"PDF to Word conversion failed: {str(e)}")
