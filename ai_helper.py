
# NOTE: This file contains example code for calling Google Cloud Vertex AI (Gemini) using the
# google-cloud-aiplatform client library. Please configure your GOOGLE_APPLICATION_CREDENTIALS
# environment variable (or run `gcloud auth application-default login`) before running.
#
# Replace the model_name / endpoint variables with the model you want to use.
#
# For the hackathon prototype, this file organizes:
# - simplify_text(text): returns a plain-English summary
# - answer_question(context, question): returns an answer using the LLM with the document as context
#
# If you prefer to test locally without GCP, you can mock these functions to return canned responses.

from typing import Dict
import os

# Import Vertex AI client
try:
    from google.cloud import aiplatform
except Exception as e:
    aiplatform = None

# Configure these for your project
GCP_PROJECT = os.environ.get('GCP_PROJECT', 'your-gcp-project-id')
GCP_REGION = os.environ.get('GCP_REGION', 'us-central1')
# Example container/endpoint/model name; change to the Vertex/Generative model you have access to
MODEL_NAME = os.environ.get('VERTEX_MODEL_NAME', 'models/text-bison@001')

def _init_client():
    if aiplatform is None:
        return None
    aiplatform.init(project=GCP_PROJECT, location=GCP_REGION)
    return aiplatform

def simplify_text(text: str) -> str:
    """Send the document text to Vertex AI to get a simplified summary.
    Returns a string summary. If Vertex client isn't available, returns a placeholder."""
    client_lib = _init_client()
    if client_lib is None:
        # running without google-cloud-aiplatform installed or configured
        return "[MOCK SUMMARY] This is a short simplified summary of the uploaded contract. (Set up GCP to get live results)"

    try:
        # Example using the Vertex AI text generation API (pseudo-code; refer to your model's API)
        from google.cloud.aiplatform.gapic.schema import predict
        # For production, use the correct Vertex client/methods for your selected GenAI model.
        # This snippet is intentionally minimal; consult Vertex AI docs for up-to-date examples.
        response = client_lib.TextGenerationModel(model_name=MODEL_NAME).call(text)
        return str(response)
    except Exception as e:
        return f"[ERROR calling Vertex AI: {e}]"

def answer_question(context: str, question: str) -> str:
    """Answer a user question using the document context as grounding. Returns the model's answer."""
    client_lib = _init_client()
    if client_lib is None:
        return "[MOCK ANSWER] This clause means: The tenant must pay rent by the 5th of every month. (Mock response)"

    try:
        prompt = f\"You are a helpful assistant. Given the following document, answer the question concisely.\n\nDocument:\n{context}\n\nQuestion:\n{question}\n\nProvide a short, user-friendly answer and highlight any potential legal risks if present.\"
        response = client_lib.TextGenerationModel(model_name=MODEL_NAME).call(prompt)
        return str(response)
    except Exception as e:
        return f"[ERROR calling Vertex AI: {e}]"
