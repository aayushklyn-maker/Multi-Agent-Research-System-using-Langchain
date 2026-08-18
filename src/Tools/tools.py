from dotenv import load_dotenv
from langchain.tools import tool
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient

load_dotenv()

def web_search(topic:str) -> str:
    """ Searches the web for recent and reliable information on given topic.
    Returns Titles,URLs and snippets."""
    