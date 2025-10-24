# web_scraper.py

import requests
from bs4 import BeautifulSoup
from typing import Dict, Any

def scrape_website_tool(url: str) -> Dict[str, Any]:
    """
    Web scraper using BeautifulSoup and requests. Used by the topic deconstructer
    agent to gather initial, broad information about a technical skill/topic.
    """
    print(f"[SCRAPER] Fetching: {url}")
    
    try:
        # Set headers to mimic a browser
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        
        # Send GET request
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        
        # Parse HTML
        soup = BeautifulSoup(response.text, 'lxml')
        
        # Extract title (try multiple common patterns)
        title = None
        if soup.find('h1'):
            title = soup.find('h1').get_text(strip=True)
        elif soup.find('title'):
            title = soup.find('title').get_text(strip=True)
        
        # Extract author (common meta tags and patterns)
        author = None
        author_meta = soup.find('meta', {'name': 'author'}) or \
                     soup.find('meta', {'property': 'article:author'}) or \
                     soup.find('span', {'class': 'author'}) or \
                     soup.find('a', {'rel': 'author'})
        if author_meta:
            # Safely extract content or text
            author = author_meta.get('content') if author_meta.get('content') else author_meta.get_text(strip=True)
        
        # Extract publish date
        date = None
        date_meta = soup.find('meta', {'property': 'article:published_time'}) or \
                   soup.find('meta', {'name': 'publish-date'}) or \
                   soup.find('time')
        if date_meta:
            date = date_meta.get('datetime') or date_meta.get('content') or date_meta.get_text(strip=True)
        
        # Extract main content (try multiple selectors)
        content = ""
        paragraphs = []
        
        # Try common article content selectors
        article_body = soup.find('article') or \
                      soup.find('div', {'class': lambda x: x and ('content' in x.lower() or 'article' in x.lower())}) or \
                      soup.find('div', {'id': lambda x: x and 'content' in x.lower()})
        
        if article_body:
            # Get all paragraphs within article
            paragraphs = article_body.find_all('p')
            content = ' '.join([p.get_text(strip=True) for p in paragraphs if len(p.get_text(strip=True)) > 50])
        else:
            # Fallback: get all paragraphs
            paragraphs = soup.find_all('p')
            content = ' '.join([p.get_text(strip=True) for p in paragraphs[:10] if len(p.get_text(strip=True)) > 50])
        
        # Extract domain
        from urllib.parse import urlparse
        domain = urlparse(url).netloc
        
        result = {
            "status": "success",
            "url": url,
            "domain": domain,
            "scraped_data": {
                "title": title or "No title found",
                "author": author or "Unknown",
                "date": date or "Unknown",
                "content": content[:2000] if content else "No content extracted",  # Limit to 2000 chars
                "content_length": len(content),
                "paragraphs_found": len(paragraphs)
            }
        }
        
        print(f"[SCRAPER] Success: Extracted {len(content)} characters")
        return result
        
    except requests.exceptions.RequestException as e:
        print(f"[SCRAPER] HTTP Error: {str(e)}")
        return {
            "status": "error",
            "error": f"Failed to fetch URL: {str(e)}",
            "url": url
        }
    except Exception as e:
        print(f"[SCRAPER] Parsing Error: {str(e)}")
        return {
            "status": "error",
            "error": f"Failed to parse content: {str(e)}",
            "url": url
        }

__all__ = ['scrape_website_tool']