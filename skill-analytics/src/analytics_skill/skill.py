"""Analytics skill catalog."""

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
        SkillDefinition("dashboard-analysis", "Analyze dashboards and summarize business performance trends.", "analytics", ["data", "goal"], "Dashboard summary"),
        SkillDefinition("trend-analysis", "Detect trends and patterns from historical data.", "analytics", ["data", "timeframe"], "Trend report"),
        SkillDefinition("anomaly-detector", "Highlight unusual activity, outliers, or unexpected patterns.", "operations", ["data", "threshold"], "Anomaly summary"),
        SkillDefinition("kpi-reporting", "Create KPI scorecards and business metric reporting.", "reporting", ["metrics", "target"], "KPI report"),
        SkillDefinition("executive-summary", "Summarize key business insights for leadership communication.", "reporting", ["data", "stakeholder"], "Executive brief"),
        SkillDefinition("market-insight-generator", "Generate strategic market insights from data and observations.", "strategy", ["market_data", "question"], "Market insight brief"),
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
        "Recommended steps:\n1. Validate the source data\n2. Identify key patterns\n3. Formulate insights\n4. Recommend action"
    )


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Analytics skill pack")
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
