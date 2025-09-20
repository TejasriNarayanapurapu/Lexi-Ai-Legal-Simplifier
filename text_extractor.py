
import PyPDF2

def extract_text_from_pdf(path):
    """Extracts text from a PDF using PyPDF2. Returns a single string."""
    text_parts = []
    try:
        with open(path, 'rb') as fh:
            reader = PyPDF2.PdfReader(fh)
            for page in reader.pages:
                text_parts.append(page.extract_text() or '')
    except Exception as e:
        return f"[ERROR extracting text: {e}]"
    return '\n'.join(text_parts)
