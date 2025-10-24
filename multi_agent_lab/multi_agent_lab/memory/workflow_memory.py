import json
from datetime import datetime

class IntegrityWorkflowMemory:
    def __init__(self):
        self.data = {
            "skill_topic_input": None,         # Input topic for the roadmap
            "deconstructed_modules": None,     # Output of topic_deconstructer_agent
            "prerequisites": None,             # Output of prerequisite_validator_agent
            "core_concepts": None,             # Output of concepts_researcher_agent
            "project_ideas": None,             # Output of project_generator_agent
            "learning_resources": None,        # Output of resource_curator_agent
            "final_report": None,              # Output of roadmap_architect_critic_agent
            "execution_logs": []
        }
    def store(self, key, value):
        self.data[key] = value
        self.log_event(f"Stored '{key}'")
    def retrieve(self, key):
        # Fallback to allow retrieving old keys if needed, though not recommended
        return self.data.get(key)
    def log_event(self, message, level="INFO"):
        self.data["execution_logs"].append({
            "timestamp": datetime.now().isoformat(), 
            "message": message,
            "level": level
        })
    def get_snapshot(self):
        return self.data.copy()
    def export_reports(self, filename="learning_roadmap_results.json"):
        # Changed default filename to match the new workflow's output
        with open(filename, 'w') as f:
            json.dump(self.data, f, indent=2)
        return filename

workflow_memory = IntegrityWorkflowMemory()