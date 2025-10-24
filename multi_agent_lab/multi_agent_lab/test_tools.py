from tools.web_scraper import scrape_website_tool
from tools.web_searcher import web_search_tool

# Test scraper
print("Testing Web Scraper...")
result1 = scrape_website_tool("https://en.wikipedia.org/wiki/Artificial_intelligence")
print(f"Title: {result1['scraped_data']['title']}")
print(f"Content length: {result1['scraped_data']['content_length']}")

# Test search
print("\nTesting Web Search...")
result2 = web_search_tool("artificial intelligence latest news")
print(f"Found {len(result2['results'])} results")
for i, r in enumerate(result2['results'][:3], 1):
    print(f"{i}. {r['title']}")
