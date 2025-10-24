import os
import requests
from typing import Dict, Any, List

def web_search_tool(query: str, num_results: int = 10) -> Dict[str, Any]:
    """
    Real web search using Serper.dev API (Google Search)
    Get API key from: https://serper.dev (Free tier: 2500 searches/month)
    Set environment variable: SERPER_API_KEY
    """
    print(f"[WEB_SEARCH] Searching: {query}")
    
    api_key = os.getenv('SERPER_API_KEY')
    
    if not api_key:
        print("[WEB_SEARCH] Warning: SERPER_API_KEY not found. Using mock data.")
        # Fallback to mock data if no API key
        return _mock_search_results(query)
    
    try:
        url = "https://google.serper.dev/search"
        
        payload = {
            "q": query,
            "num": num_results
        }
        
        headers = {
            'X-API-KEY': api_key,
            'Content-Type': 'application/json'
        }
        
        response = requests.post(url, json=payload, headers=headers, timeout=10)
        response.raise_for_status()
        
        data = response.json()
        
        # Extract organic results
        results = []
        if 'organic' in data:
            for item in data['organic'][:num_results]:
                results.append({
                    "title": item.get('title', ''),
                    "snippet": item.get('snippet', ''),
                    "url": item.get('link', ''),
                    "source": item.get('displayedLink', ''),
                    "date": item.get('date', 'Unknown')
                })
        
        print(f"[WEB_SEARCH] Found {len(results)} results")
        
        return {
            "status": "success",
            "query": query,
            "total_results": len(results),
            "results": results
        }
        
    except Exception as e:
        print(f"[WEB_SEARCH] Error: {str(e)}")
        return {
            "status": "error",
            "error": str(e),
            "query": query
        }

def _mock_search_results(query: str) -> Dict[str, Any]:
    """Fallback mock results if no API key"""
    return {
        "status": "success",
        "query": query,
        "note": "Mock results - Set SERPER_API_KEY for real search",
        "results": [
            {
                "title": f"Comprehensive analysis of {query}",
                "snippet": f"Detailed information about {query} from reputable sources.",
                "url": f"https://example-news.com/analysis-{query.replace(' ', '-')}",
                "source": "example-news.com",
                "date": "2025-10-24"
            },
            {
                "title": f"Expert perspective on {query}",
                "snippet": f"In-depth research and findings about {query}.",
                "url": f"https://research-journal.org/study-{query.replace(' ', '-')}",
                "source": "research-journal.org",
                "date": "2025-10-23"
            },
            {
                "title": f"Breaking: Latest updates on {query}",
                "snippet": f"Recent developments and news related to {query}.",
                "url": f"https://independent-media.net/news-{query.replace(' ', '-')}",
                "source": "independent-media.net",
                "date": "2025-10-22"
            }
        ]
    }

# Alias for compatibility with agent imports
serper_dev_tool = web_search_tool

__all__ = ['web_search_tool', 'serper_dev_tool']
