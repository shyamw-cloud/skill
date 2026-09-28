"""Customer support skill catalog."""

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
        SkillDefinition("ticket-triage", "Categorize support tickets by urgency and issue type.", "support", ["ticket", "context"], "Triage summary"),
        SkillDefinition("helpdesk-automation", "Design helpdesk automation and routing rules for common issues.", "automation", ["issue_types", "workflow"], "Automation plan"),
        SkillDefinition("response-drafter", "Draft empathetic and accurate customer responses.", "communication", ["issue", "tone"], "Customer reply draft"),
        SkillDefinition("issue-resolution-guide", "Provide a resolution path for recurring support problems.", "support", ["issue", "system"], "Resolution guide"),
        SkillDefinition("feedback-classifier", "Classify support and product feedback into themes and trends.", "analytics", ["feedback", "goal"], "Theme summary"),
        SkillDefinition("customer-health-summary", "Summarize customer account health and service risk.", "success", ["customer_data", "activity"], "Customer health summary"),
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
        "Recommended steps:\n1. Understand the issue and priority\n2. Match against known resolution patterns\n3. Draft a response or routing plan\n4. Recommend follow-up"
    )


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Customer support skill pack")
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
