
# LexiAI - Legal Document Simplifier (Hackathon Prototype)

## What this prototype does
- Upload a legal PDF (rental agreement, loan contract, etc.).
- Extracts text using PyPDF2.
- Sends the extracted text to Google Cloud Vertex AI (Gemini/text-bison etc.) to get a simplified summary.
- Provides a simple Q&A endpoint to ask questions about the document (document used as context).

## How to run (with Vertex AI integration)
1. Create a Google Cloud project and enable Vertex AI.
2. Create a Service Account and download the JSON key file.
3. Set environment variable:
   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/service-account.json"
   export GCP_PROJECT="your-gcp-project-id"
   export GCP_REGION="your-region-us-central1"
   export VERTEX_MODEL_NAME="models/text-bison@001" # or your chosen model
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Run the app:
   ```bash
   python app.py
   ```
6. Open http://127.0.0.1:5000

## If you don't want to use GCP right away
- The `utils/ai_helper.py` contains mock responses if Vertex isn't configured. This allows you to demo locally without cloud calls.

## Files included
- `app.py` - Flask app
- `utils/text_extractor.py` - PDF -> text
- `utils/ai_helper.py` - Vertex AI integration (with mock fallback)
- `templates/index.html` - Frontend
- `static/style.css` - Styling
- `sample_docs/` - placeholder sample files (replace with real PDFs)
