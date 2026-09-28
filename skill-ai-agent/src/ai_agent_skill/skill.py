"""AI agent skill catalog."""

from dataclasses import dataclass
from typing import List


@dataclass(frozen=True)
class SkillDefinition:
    name: str
    description: str
    category: str
    inputs: List[str]
    output: str


def get_skill_catalog() -> List[SkillDefinition]:
    return [
        SkillDefinition("prompt-optimizer", "Improve prompts for higher-quality, lower-noise AI outputs.", "ai-agent", ["prompt", "goal"], "Improved prompt"),
        SkillDefinition("tool-router", "Choose the correct tool or workflow for an AI task.", "ai-agent", ["task", "available_tools"], "Tool routing recommendation"),
        SkillDefinition("multi-agent-planner", "Break a large problem into steps coordinated by multiple agents.", "ai-agent", ["task", "constraints"], "Agent plan"),
        SkillDefinition("workflow-coordinator", "Coordinate steps, dependencies, and execution flow for agent tasks.", "orchestration", ["workflow", "tasks"], "Workflow plan"),
        SkillDefinition("knowledge-base-curator", "Organize and update a repository of facts, policies, and references.", "knowledge", ["documents", "topic"], "Curated knowledge base"),
        SkillDefinition("reasoning-assistant", "Support structured reasoning, decision-making, and tradeoff analysis.", "reasoning", ["problem", "decision_context"], "Reasoned recommendation"),
    ]


def run_skill(skill_name: str, prompt: str) -> str:
    catalog = {item.name: item for item in get_skill_catalog()}
    skill = catalog.get(skill_name)
    if skill is None:
        return f"Unknown skill '{skill_name}'. Available: {', '.join(sorted(catalog))}."
    return (
        f"Skill: {skill.name}\n"
        f"Category: {skill.category}\n"
        f"Description: {skill.description}\n\n"
        f"Request:\n{prompt}\n\n"
        "Recommended steps:\n1. Define the objective\n2. Choose the right tool or agent\n3. Structure the workflow\n4. Validate the outcome"
    )


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="AI agent skill pack")
    parser.add_argument("--list", action="store_true")
    parser.add_argument("--skill")
    parser.add_argument("--prompt")
    args = parser.parse_args()
    if args.list:
        for item in get_skill_catalog():
            print(f"- {item.name}: {item.description}")
    elif args.skill:
        print(run_skill(args.skill, args.prompt or "No prompt supplied."))
    else:
        parser.print_help()
