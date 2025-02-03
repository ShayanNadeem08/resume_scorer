from fastapi import FastAPI, File, UploadFile
import pdfplumber

app = FastAPI()

@app.post("/upload/")
async def upload_resume(file: UploadFile = File(...)):
    text = ""
    if file.filename.endswith(".pdf"):
        with pdfplumber.open(file.file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() + "\n"
    return {"filename": file.filename, "extracted_text": text}
