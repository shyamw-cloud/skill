"""Customer success skill catalog."""

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
        SkillDefinition("customer-health-score", "Build a customer health score using engagement, sentiment, and product usage data.", "success", ["customer_data", "criteria"], "Health score summary"),
        SkillDefinition("renewal-risk-analyzer", "Estimate churn and renewal risk for active customers.", "success", ["history", "customer_activity"], "Renewal risk report"),
        SkillDefinition("onboarding-roadmap", "Create onboarding milestones and success checkpoints for new accounts.", "enablement", ["customer_goal", "timeline"], "Onboarding roadmap"),
        SkillDefinition("usage-pattern-analyzer", "Identify product usage patterns and gaps in customer adoption.", "analytics", ["usage_data", "goal"], "Usage analysis"),
        SkillDefinition("success-plan-builder", "Design success plans for strategic or at-risk accounts.", "strategy", ["account_info", "goals"], "Success plan"),
        SkillDefinition("churn-risk-review", "Review churn signals and recommend mitigation actions.", "risk", ["customer_data", "signals"], "Churn risk overview"),
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
        "Recommended steps:\n1. Assess customer context\n2. Review engagement and risk indicators\n3. Identify actions and owners\n4. Recommend next-step plan"
    )


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Customer success skill pack")
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
