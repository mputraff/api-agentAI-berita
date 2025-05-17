from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.extractor import extract_article
from app.summarizer import summarize_text

router = APIRouter()

class SummarizeRequest(BaseModel):
    url: str

@router.post("/summarize")
async def summarize(request: SummarizeRequest):
    try:
        article = extract_article(request.url)
        summary = summarize_text(article)
        return {"summary": summary}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))