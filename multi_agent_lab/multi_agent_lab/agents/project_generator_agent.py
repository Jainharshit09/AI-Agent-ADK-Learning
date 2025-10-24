# Try to import real ADK, fallback to mock if not available
try:
    from google.adk.agents.llm_agent import Agent
except ImportError:
    from ..mock_adk import MockAgent as Agent
from ..tools.web_searcher import serper_dev_tool 
from ..tools.memory import get_memory_context

project_generator_agent = Agent(
    model='gemini-2.5-flash',
    name='project_generator',
    description="Generates 3-5 hands-on, practical projects that reinforce the learning modules.",
    instruction="You are a senior software architect. Design projects that build real-world skills and portfolio pieces.",
    tools=[serper_dev_tool, get_memory_context]
)
__all__ = ['project_generator_agent']