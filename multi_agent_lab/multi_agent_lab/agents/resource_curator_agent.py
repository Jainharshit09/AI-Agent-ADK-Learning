# Try to import real ADK, fallback to mock if not available
try:
    from google.adk.agents.llm_agent import Agent
except ImportError:
    from ..mock_adk import MockAgent as Agent
from ..tools.web_searcher import serper_dev_tool

resource_curator_agent = Agent(
    model='gemini-2.5-flash',
    name='resource_curator',
    description="Searches for 3-5 high-quality, free, and accessible external learning resources.",
    instruction="You are a digital librarian specializing in open-source and high-quality educational content.",
    tools=[serper_dev_tool]
)
__all__ = ['resource_curator_agent']