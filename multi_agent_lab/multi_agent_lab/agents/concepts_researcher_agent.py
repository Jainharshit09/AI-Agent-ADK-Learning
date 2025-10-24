# Try to import real ADK, fallback to mock if not available
try:
    from google.adk.agents.llm_agent import Agent
except ImportError:
    from ..mock_adk import MockAgent as Agent
from ..tools.web_searcher import serper_dev_tool 
from ..tools.memory import get_memory_context

concepts_researcher_agent = Agent(
    model='gemini-2.5-flash',
    name='concepts_researcher',
    description="Research high-level modules and fill them with 5-7 specific, current concepts or technologies.",
    instruction="You are a cutting-edge industry analyst. Find the most relevant technologies and concepts.",
    tools=[serper_dev_tool, get_memory_context]
)
__all__ = ['concepts_researcher_agent']