"""HR skill catalog."""

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
        SkillDefinition("hiring-assistant", "Support hiring workflows, candidate screening, and interview planning.", "recruiting", ["role", "team_context"], "Hiring plan"),
        SkillDefinition("onboarding-planner", "Design onboarding steps, tasks, and schedules for new employees.", "people-ops", ["role", "start_date"], "Onboarding plan"),
        SkillDefinition("performance-review-analyzer", "Summarize employee performance themes and feedback patterns.", "people-ops", ["feedback_data", "goal"], "Review summary"),
        SkillDefinition("employee-engagement-insights", "Identify employee engagement risks and improvement opportunities.", "engagement", ["survey_data", "context"], "Engagement insight brief"),
        SkillDefinition("talent-pipeline-review", "Review hiring pipeline health and improvement opportunities.", "recruiting", ["pipeline_data", "goal"], "Pipeline review"),
        SkillDefinition("policy-clarifier", "Clarify HR policies and provide employee-facing guidance.", "compliance", ["policy", "question"], "Policy explanation"),
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
        "Recommended steps:\n1. Define objective\n2. Gather policy or data context\n3. Identify risks or opportunities\n4. Produce recommended action"
    )


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="HR skill pack")
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
