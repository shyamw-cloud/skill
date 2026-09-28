"""Product and strategy skill catalog."""

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
        SkillDefinition("roadmap-builder", "Outline product roadmap priorities and strategic milestones.", "product", ["theme", "constraints"], "Roadmap plan"),
        SkillDefinition("feature-prioritizer", "Rank features by customer value, effort, and strategic impact.", "product", ["ideas", "criteria"], "Prioritized backlog"),
        SkillDefinition("competitive-analysis", "Summarize competitors, differentiation, and strategic threats.", "strategy", ["market", "competitors"], "Competitive brief"),
        SkillDefinition("pricing-strategy", "Recommend pricing strategies based on market position and value.", "strategy", ["offer", "market"], "Pricing recommendation"),
        SkillDefinition("customer-interview-summarizer", "Turn customer conversations into themes, pain points, and opportunities.", "research", ["interviews", "goal"], "Interview summary"),
        SkillDefinition("decision-support-assistant", "Support strategic decision-making with tradeoff analysis and options.", "decision", ["problem", "options"], "Decision memo"),
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
        "Recommended steps:\n1. Clarify the product or strategy question\n2. Review evidence and constraints\n3. Compare options\n4. Recommend a path"
    )


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Product and strategy skill pack")
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
