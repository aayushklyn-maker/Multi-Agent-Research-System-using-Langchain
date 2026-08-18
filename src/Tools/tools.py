from dotenv import load_dotenv
from langchain.tools import tool
import requests
import rich
from rich import print
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os
load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

@tool
def web_search(topic:str) -> str:
    """ Searches the web for recent and reliable information on given topic.
    Returns Titles,URLs and snippets."""
    try:
        search_result = tavily.search(
            query = topic,
            search_depth="basic",
            max_results=5,
            topic="news"
        )
        results = search_result['results']
        out = []
        for r in results:
            out.append(f"Title : {r['title']}\n"
                  f"URL : {r['url']}\n"
                  f"snippet : {r['content'][:300]}\n")
        return "\n----------------\n".join(out)

    except Exception as e:
        return f"Could not fetch details for {topic} : {str(e)}"

@tool
def scrape_url(url:str) -> str:
    """ Extracts detailed information from url in proper format """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }
    try:
        response = requests.get(url,headers=headers,timeout=6)
        soup = BeautifulSoup(response.text,"html.parser")
        for tag in soup(['script','noscript','style','header','footer','nav']):
            tag.decompose()
        text = soup.get_text(separator=" ",strip=True)[:3000]
        return text

    except Exception as e:
        return f"Could not scrape information from URL : {str(e)}"
