# Try to import real ADK, fallback to mock if not available
from google.adk.agents.llm_agent import Agent
from ..tools.memory import get_memory_context

prerequisite_validator_agent = Agent(
    model='gemini-2.5-flash',
    name='prerequisite_validator',
    description="Identifies 3-5 non-negotiable prerequisite skills for a given set of learning modules.",
    instruction="You are a senior technical interviewer. Identify the essential foundational knowledge required.",
    tools=[get_memory_context]
)
__all__ = ['prerequisite_validator_agent']