# memory.py

from ..memory.workflow_memory import workflow_memory

def get_memory_context() -> dict:
    """Returns current shared workflow memory snapshot for an agent to use as context."""
    return {"status": "success", "context": workflow_memory.get_snapshot()}

__all__ = ['get_memory_context']