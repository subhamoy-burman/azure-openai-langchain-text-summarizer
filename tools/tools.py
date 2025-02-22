from langchain_community.tools.tavily_search import TavilySearchResults

def get_profile_url_tavily(name: str) -> str:
    search = TavilySearchResults()
    search_results = search.run(f"{name}")
    return search_results