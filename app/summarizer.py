import os
from dotenv import load_dotenv
from google.oauth2 import service_account
import vertexai
from vertexai.generative_models import GenerativeModel

# Load environment
load_dotenv()

# Konfigurasi kredensial dan project
credentials = service_account.Credentials.from_service_account_file(
    os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
)

vertexai.init(
    project=os.getenv("GCP_PROJECT_ID"),
    location=os.getenv("GCP_LOCATION"),
    credentials=credentials
)

# Inisialisasi model Gemini terbaru
model = GenerativeModel("gemini-2.5-pro-preview-05-06")

# Fungsi untuk membuat ringkasan dari artikel
def summarize_text(article: str) -> str:
    prompt = f"""
    Berikut adalah isi sebuah artikel berita:

    {article}

    Buatlah ringkasan dari artikel tersebut dalam bahasa Indonesia yang mudah dipahami.
    """
    
    response = model.generate_content(prompt)
    
    return response.text.strip()