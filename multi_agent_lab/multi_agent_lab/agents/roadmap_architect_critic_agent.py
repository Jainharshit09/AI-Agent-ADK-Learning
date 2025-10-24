# Try to import real ADK, fallback to mock if not available
from google.adk.agents.llm_agent import Agent
from ..tools.memory import get_memory_context

roadmap_architect_critic_agent = Agent(
    model='gemini-2.5-flash',
    name='roadmap_architect_critic',
    description="Gathers all outputs and synthesizes them into a final, structured 'Learning Roadmap'.",
    instruction="You are the final editor-in-chief. Ensure the final roadmap is logical, complete, and provides maximum educational value.",
    tools=[get_memory_context]
)
__all__ = ['roadmap_architect_critic_agent']