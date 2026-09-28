"""Operations skill catalog."""

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
        SkillDefinition("process-mapping", "Map workflows and identify bottlenecks across operational processes.", "operations", ["workflow", "pain_points"], "Process map"),
        SkillDefinition("resource-planning", "Plan staffing, capacity, and assignments for operational goals.", "operations", ["demand", "team"], "Resource plan"),
        SkillDefinition("vendor-management", "Review vendor performance and operational dependencies.", "procurement", ["vendor_data", "service"], "Vendor review"),
        SkillDefinition("capacity-analysis", "Assess operational capacity and demand balance.", "planning", ["load", "capacity"], "Capacity analysis"),
        SkillDefinition("service-level-review", "Review service delivery quality and SLA performance.", "operations", ["service_data", "target"], "Service review"),
        SkillDefinition("incident-prioritization", "Prioritize incidents or operational issues by urgency and impact.", "operations", ["issue_data", "severity"], "Priority list"),
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
        "Recommended steps:\n1. Define the operating objective\n2. Review process or capacity constraints\n3. Identify bottlenecks\n4. Recommend action plan"
    )


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Operations skill pack")
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
