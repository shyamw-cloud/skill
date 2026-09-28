"""Sales skill catalog."""

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
        SkillDefinition("lead-prioritization", "Score and rank leads based on urgency, fit, and opportunity value.", "sales", ["leads", "criteria"], "Prioritized lead list"),
        SkillDefinition("sales-forecast", "Predict pipeline and revenue outcomes over a set period.", "forecasting", ["history", "timeframe"], "Revenue forecast"),
        SkillDefinition("proposal-generator", "Draft proposals tailored to customer needs and buying context.", "sales", ["customer_context", "offer"], "Proposal draft"),
        SkillDefinition("pipeline-review", "Assess pipeline health and identify common bottlenecks.", "sales", ["pipeline_data", "goal"], "Pipeline review"),
        SkillDefinition("renewal-risk-analyzer", "Estimate customer renewal risk using account health and behavioral signals.", "customer-success", ["account_data", "history"], "Renewal risk assessment"),
        SkillDefinition("sales-enablement", "Create sales enablement tools, scripts, and guidance for the sales team.", "enablement", ["persona", "offer"], "Enablement package"),
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
        "Recommended steps:\n1. Review current pipeline context\n2. Prioritize opportunities\n3. Outline action plan\n4. Recommend next steps"
    )


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Sales skill pack")
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
