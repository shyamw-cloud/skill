"""Business skill catalog for enterprise workflow and analytics skills."""

from __future__ import annotations

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
        SkillDefinition(
            name="business-analytics",
            description="Analyze business performance, KPIs, and trends to produce action-oriented insights.",
            category="analytics",
            inputs=["data", "business_goal"],
            output="KPI summary and insight report",
        ),
        SkillDefinition(
            name="sales-forecasting",
            description="Forecast sales pipeline, demand, and expected revenue over a period.",
            category="sales",
            inputs=["history", "time_period"],
            output="Forecast and recommendations",
        ),
        SkillDefinition(
            name="crm-automation",
            description="Automate customer record updates, lead handling, and CRM workflows.",
            category="crm",
            inputs=["customer_data", "workflow"],
            output="CRM workflow plan and automation steps",
        ),
        SkillDefinition(
            name="financial-analysis",
            description="Review spending, budgets, return on investment, and financial trends.",
            category="finance",
            inputs=["financial_data", "metric"],
            output="Financial findings and recommendations",
        ),
        SkillDefinition(
            name="document-extraction",
            description="Extract and structure data from invoices, forms, PDFs, and business documents.",
            category="automation",
            inputs=["document_type", "content"],
            output="Extracted structured fields",
        ),
        SkillDefinition(
            name="workflow-optimization",
            description="Identify process bottlenecks and recommend workflow improvements.",
            category="operations",
            inputs=["process", "problems"],
            output="Process redesign and efficiency plan",
        ),
        SkillDefinition(
            name="sentiment-analysis",
            description="Analyze customer feedback, reviews, and surveys to assess sentiment.",
            category="customer-insights",
            inputs=["feedback_text", "goal"],
            output="Sentiment summary and themes",
        ),
        SkillDefinition(
            name="inventory-forecasting",
            description="Forecast inventory demand and recommend reorder or stock planning actions.",
            category="supply-chain",
            inputs=["inventory_data", "lead_time"],
            output="Inventory forecast and recommendations",
        ),
    ]


def run_skill(skill_name: str, prompt: str) -> str:
    catalog = {item.name: item for item in get_skill_catalog()}
    skill = catalog.get(skill_name)
    if skill is None:
        options = ", ".join(sorted(catalog))
        return f"Unknown skill '{skill_name}'. Available skills: {options}."

    return (
        f"Skill: {skill.name}\n"
        f"Category: {skill.category}\n"
        f"Description: {skill.description}\n\n"
        f"Request:\n{prompt}\n\n"
        "Recommended process:\n"
        "1. Define the business objective and constraints.\n"
        "2. Review available data and system context.\n"
        "3. Transform data into insights or automation steps.\n"
        "4. Highlight risks, assumptions, and next actions."
    )


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Business skill catalog")
    parser.add_argument("--list", action="store_true", help="List skills")
    parser.add_argument("--skill", help="Skill to execute")
    parser.add_argument("--prompt", help="Task prompt")
    args = parser.parse_args()

    if args.list:
        for skill in get_skill_catalog():
            print(f"- {skill.name}: {skill.description}")
    elif args.skill:
        print(run_skill(args.skill, args.prompt or "No prompt supplied."))
    else:
        parser.print_help()
