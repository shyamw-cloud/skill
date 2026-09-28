"""Finance skill catalog."""

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
        SkillDefinition("budget-analysis", "Review budgets against actuals and highlight variances.", "finance", ["budget", "actuals"], "Budget variance summary"),
        SkillDefinition("cashflow-forecasting", "Forecast inflows and outflows over a time horizon.", "finance", ["cash_data", "period"], "Cash flow forecast"),
        SkillDefinition("roi-review", "Assess investment return and strategic value.", "finance", ["investment", "returns"], "ROI analysis"),
        SkillDefinition("expense-optimizer", "Find savings opportunities across expenses and operating costs.", "operations", ["expense_data", "goal"], "Savings plan"),
        SkillDefinition("variance-analysis", "Break down cost and revenue variance against expectations.", "analysis", ["actuals", "baseline"], "Variance report"),
        SkillDefinition("financial-planning", "Support planning for budgets, capital allocation, and risk-reduction.", "planning", ["context", "goals"], "Financial plan"),
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
        "Recommended steps:\n1. Review source financial data\n2. Compare against targets\n3. Diagnose variance\n4. Recommend a correction plan"
    )


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Finance skill pack")
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
