# workflow.py

import asyncio

# Try to import real ADK, fallback to mock if not available
try:
    from google.adk.sessions import InMemorySessionService
    from google.adk.runners import Runner
    from google.genai.types import Content, Part
    print("Using real Google ADK")
except ImportError:
    print("Google ADK not found, using mock implementation")
    from .mock_adk import MockSessionService as InMemorySessionService, MockRunner as Runner, MockContent as Content, MockPart as Part
# Import the aliased orchestrator and memory from the new agent.py
from .agent import (
    root_orchestrator_agent,
    workflow_memory
)

session_service = InMemorySessionService()

async def run_roadmap_generator_workflow(skill_topic: str) -> dict:
    """Execute complete Technical Learning Roadmap Generator workflow"""
    
    print("\n" + "="*80)
    print("TECHNICAL LEARNING ROADMAP GENERATOR - ADK IMPLEMENTATION")
    print("="*80)
    print(f"Target Skill/Topic: {skill_topic}\n")
    
    # Store skill topic in memory
    # Renamed the key from "url_input" to "skill_topic_input" to match the new memory structure
    workflow_memory.store("skill_topic_input", skill_topic)
    workflow_memory.log_event(f"WORKFLOW_START: Generating roadmap for {skill_topic}", "INFO")
    
    try:
        # Create session
        session = await session_service.create_session(
            app_name="roadmap_generator", # Updated app name
            user_id="architect",          # Updated user ID
            session_id="roadmap_workflow" # Updated session ID
        )
        workflow_memory.log_event(f"SESSION_CREATED: {session.id}", "INFO")
        
        # Initialize runner with root orchestrator
        runner = Runner(
            agent=root_orchestrator_agent,
            app_name="roadmap_generator", # Updated app name
            session_service=session_service
        )
        
        # Prepare workflow message for the new orchestrator
        workflow_message = Content(
            role='user',
            parts=[Part(text=f"Please generate a comprehensive learning roadmap for the skill/topic: {skill_topic}\n\n" +
                           "Complete the full multi-agent workflow: deconstruct topic, validate prerequisites, " +
                           "run parallel research (concepts, projects, resources), and synthesize the final structured Markdown report.")]
        )
        
        # Execute workflow
        workflow_memory.log_event("ORCHESTRATOR_INITIALIZED", "INFO")
        print("Executing roadmap generation phases...\n")
        
        final_response = ""
        phase_count = 0
        
        async for event in runner.run_async(
            user_id="architect",
            session_id=session.id,
            new_message=workflow_message
        ):
            if event.is_final_response() and event.content and event.content.parts:
                final_response = event.content.parts[0].text
                phase_count += 1
        
        workflow_memory.log_event("ORCHESTRATOR_COMPLETED", "INFO")
        
        # Generate reports
        memory_snapshot = workflow_memory.get_snapshot()
        # Updated default filename
        report_file = workflow_memory.export_reports(filename="learning_roadmap_results.json")
        
        print("\n" + "-"*80)
        print("WORKFLOW EXECUTION COMPLETE")
        print("-"*80)
        print("\nFINAL LEARNING ROADMAP:\n")
        print(final_response)
        print("\n" + "-"*80)
        print(f"Full workflow state exported to: {report_file}")
        print(f"Total execution events: {len(memory_snapshot['execution_logs'])}")
        print("="*80 + "\n")
        
        return {
            "status": "success",
            "report": final_response,
            "session_id": session.id,
            "report_file": report_file,
            "total_events": len(memory_snapshot['execution_logs']),
            "memory_state": memory_snapshot
        }
        
    except Exception as e:
        workflow_memory.log_event(f"CRITICAL_ERROR: {str(e)}", "ERROR")
        print(f"\nWORKFLOW ERROR: {str(e)}\n")
        return {
            "status": "error",
            "error": str(e),
            "execution_logs": workflow_memory.data["execution_logs"]
        }

# Example usage
if __name__ == "__main__":
    # Test with example skills/topics
    test_topics = [
        "Advanced Generative AI Models and Deployment",
        "Modern Full-Stack Development with React and Serverless"
    ]
    
    # Run first example
    asyncio.run(run_roadmap_generator_workflow(test_topics[0]))