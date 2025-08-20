# FastAPI Markdownify

## Overview

FastAPI Markdownify is a simple web service that converts HTML from a given URL into Markdown format. It uses FastAPI for the server and the `markdownify` library for HTML-to-Markdown conversion. This technique is useful in knowledgebase RAG AI applications.

## Features

- Accepts POST requests at `/markdown`
- Expects a JSON body with a `url` field
- Fetches the HTML content from the provided URL
- Converts HTML to Markdown using `markdownify`
- Returns the Markdown and page metadata as a response

## Usage

### Start the server

```bash
uvicorn main:app --reload
```

### Example Request

```bash
curl -X POST "http://localhost:8001/markdown" \
    -H "Content-Type: application/json" \
    -d '{"url": "https://example.com"}'
```

### Example Response

```json
{
  "source": "https://example.com",
  "title": "Example page title",
  "description": "Example meta description",
  "markdown": "# Example Domain\n\nThis domain is for use in illustrative examples in documents..."
}
```

## Requirements

- Python 3.7+
- FastAPI
- markdownify
- langchain
- lanchain-community

Install dependencies:

```bash
pip install -r requirements.txt
```

## Deployment

### Deploy using Docker

```bash
docker compose build
docker compose up -d
```
