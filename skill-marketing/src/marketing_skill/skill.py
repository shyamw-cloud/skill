"""Marketing skill catalog."""

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
        SkillDefinition("campaign-planner", "Create a campaign plan and message framework for a target audience.", "marketing", ["goal", "audience"], "Campaign outline"),
        SkillDefinition("content-strategy", "Plan content themes, channels, and priorities for marketing growth.", "marketing", ["brand", "audience"], "Content plan"),
        SkillDefinition("seo-audit", "Review search visibility, landing page optimization, and ranking opportunities.", "seo", ["site_url", "keywords"], "SEO audit"),
        SkillDefinition("audience-segmentation", "Segment customers by profile, intent, and engagement behavior.", "analytics", ["customer_data", "criteria"], "Audience segments"),
        SkillDefinition("brand-positioning", "Clarify brand positioning and messaging differentiation.", "strategy", ["market", "product"], "Positioning statement"),
        SkillDefinition("lead-nurture-planner", "Design a lead nurturing sequence to support conversion.", "sales", ["lead_stage", "goals"], "Nurture plan"),
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
        "Recommended steps:\n1. Define objective\n2. Assess target audience\n3. Choose channels\n4. Create action plan"
    )


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Marketing skill pack")
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
