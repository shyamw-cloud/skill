"""Procurement skill catalog."""

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
        SkillDefinition("vendor-evaluation", "Assess vendors across value, risk, delivery, and support quality.", "procurement", ["vendors", "criteria"], "Vendor comparison"),
        SkillDefinition("sourcing-plan", "Design sourcing and supplier selection strategies for a requirement.", "procurement", ["need", "budget"], "Sourcing plan"),
        SkillDefinition("contract-optimizer", "Review spending and contract structure for savings opportunities.", "finance", ["contracts", "costs"], "Contract optimization"),
        SkillDefinition("supplier-risk-review", "Identify supplier concentration, dependency, and delivery risks.", "risk", ["supplier_data", "context"], "Supplier risk review"),
        SkillDefinition("purchase-analysis", "Analyze purchase patterns and opportunities for efficiency or consolidation.", "operations", ["purchase_data", "goal"], "Purchase analysis"),
        SkillDefinition("negotiation-support", "Prepare a negotiation position and decision framework for procurement.", "strategy", ["supplier", "goals"], "Negotiation support plan"),
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
        "Recommended steps:\n1. Define requirement and sourcing objective\n2. Compare supplier options\n3. Assess risk and value\n4. Recommend next action"
    )


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Procurement skill pack")
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
