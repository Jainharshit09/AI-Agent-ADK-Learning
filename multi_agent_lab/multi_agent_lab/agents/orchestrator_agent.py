# Try to import real ADK, fallback to mock if not available
from google.adk.agents.llm_agent import Agent
# Importing all agents from the new Roadmap workflow
from .topic_deconstructer_agent import topic_deconstructer_agent
from .prerequisite_validator_agent import prerequisite_validator_agent
from .concepts_researcher_agent import concepts_researcher_agent
from .project_generator_agent import project_generator_agent
from .resource_curator_agent import resource_curator_agent
from .roadmap_architect_critic_agent import roadmap_architect_critic_agent
from ..memory.workflow_memory import workflow_memory # Reusing the memory object

root_agent = Agent(
    model='gemini-2.5-flash',
    name='root_orchestrator',
    description="Orchestrates the Technical Learning Roadmap Generator workflow",
    instruction="""You coordinate the multi-agent roadmap generation workflow:
    1. Deconstruct the topic and validate prerequisites (Sequential).
    2. Run parallel research (Concepts, Projects, Resources).
    3. Synthesize the final structured Learning Roadmap.
    Maintain memory context and log transitions across all agents."""
)
__all__ = ['root_agent']