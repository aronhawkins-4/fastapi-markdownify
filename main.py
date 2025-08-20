from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_community.document_loaders import AsyncHtmlLoader
from langchain_community.document_transformers import MarkdownifyTransformer
from fastapi.middleware.cors import CORSMiddleware
import uvicorn

app = FastAPI()


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class UrlRequest(BaseModel):
    url: str


@app.post("/markdown")
async def get_markdown(request: UrlRequest):
    url = request.url
    if not url or not url.startswith("http"):
        raise HTTPException(status_code=400, detail="Invalid URL")
    loader = AsyncHtmlLoader(url)
    docs = await loader.aload()  # Use async version
    md = MarkdownifyTransformer(strip=['a'])
    converted_docs = md.transform_documents(docs)
    return {"source": converted_docs[0].metadata["source"], "title": converted_docs[0].metadata["title"], "description": converted_docs[0].metadata["description"], "markdown": converted_docs[0].page_content}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
