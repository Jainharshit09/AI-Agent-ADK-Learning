# Try to import real ADK, fallback to mock if not available
from google.adk.agents.llm_agent import Agent

# Import orchestrator and sub-agents
from .agents.orchestrator_agent import root_agent as root_orchestrator_agent
from .agents.topic_deconstructer_agent import topic_deconstructer_agent
from .agents.prerequisite_validator_agent import prerequisite_validator_agent
from .agents.concepts_researcher_agent import concepts_researcher_agent
from .agents.project_generator_agent import project_generator_agent
from .agents.resource_curator_agent import resource_curator_agent
from .agents.roadmap_architect_critic_agent import roadmap_architect_critic_agent

# Import workflow memory
from .memory.workflow_memory import workflow_memory

# Import tools
from .tools.web_scraper import scrape_website_tool
from .tools.web_searcher import serper_dev_tool
from .tools.memory import get_memory_context

# Publicly exposed symbols for the ADK framework
__all__ = [
    'root_orchestrator_agent',
    'topic_deconstructer_agent',
    'prerequisite_validator_agent',
    'concepts_researcher_agent',
    'project_generator_agent',
    'resource_curator_agent',
    'roadmap_architect_critic_agent',
    'workflow_memory',
    'scrape_website_tool',
    'serper_dev_tool',
    'get_memory_context',
    'root_agent',  # Added for ADK compatibility
]

# ---------------------------------------------------------------------------
# ✅ ADK expects a variable named `root_agent` as the system entry point.
#    The orchestrator agent is our root agent, so we alias it here.
# ---------------------------------------------------------------------------
root_agent = root_orchestrator_agent
