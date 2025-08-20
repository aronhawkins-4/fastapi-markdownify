import json
from scrapegraphai.graphs import SmartScraperGraph, ScriptCreatorGraph

# Define the configuration for the scraping pipeline
graph_config = {
    "llm": {
        "model": "ollama/llama3.2",
        "model_tokens": 8192
    },
    "verbose": True,
    "headless": True,
    "library": "beautifulsoup4"
}


script_creator_graph = ScriptCreatorGraph(
    prompt="Create a Python script to scrape all pages on the website.",
    source="https://sidekick.agency/sitemap.xml",
    config=graph_config,
)

result = script_creator_graph.run()
print(result)
