"""Data engineering skill catalog."""

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
        SkillDefinition("data-pipeline-builder", "Design a pipeline to move and transform data across systems.", "data-engineering", ["sources", "targets"], "Pipeline design"),
        SkillDefinition("etl-design", "Create ETL patterns for extraction, transformation, and load operations.", "etl", ["data_sources", "business_rules"], "ETL design"),
        SkillDefinition("schema-designer", "Design normalized or analytical schemas for data storage.", "data-modeling", ["domain", "consumers"], "Schema design"),
        SkillDefinition("data-quality-audit", "Review quality issues, anomalies, and missing data patterns.", "quality", ["datasets", "rules"], "Quality audit"),
        SkillDefinition("warehouse-planning", "Plan a modern warehousing or analytics layer for business data.", "architecture", ["domain", "query_needs"], "Warehouse plan"),
        SkillDefinition("streaming-architecture", "Design event-driven streaming patterns for near-real-time data.", "architecture", ["events", "latency"], "Streaming design"),
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
        "Recommended steps:\n1. Define source and destination systems\n2. Validate schema and data contracts\n3. Define transformation logic\n4. Include quality and monitoring checks"
    )


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Data engineering skill pack")
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
