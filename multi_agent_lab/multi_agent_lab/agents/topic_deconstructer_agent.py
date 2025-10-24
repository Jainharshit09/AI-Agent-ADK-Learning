from google.adk.agents.llm_agent import Agent
# Note: Assuming scrape_website_tool is defined in a 'tools' module
from ..tools.web_scraper import scrape_website_tool 

topic_deconstructer_agent = Agent(
    model='gemini-2.5-flash',
    name='topic_deconstructer',
    description="Analyze the user's high-level technical skill or topic and break it down into 4 high-level modules.",
    instruction="You are a curriculum architect. Take a broad technical domain and define its key structural learning components.",
    tools=[scrape_website_tool]
)
__all__ = ['topic_deconstructer_agent']