"""Development skill catalog for engineering-related Smithery skills."""

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
            name="refactor",
            description="Refactor code to improve maintainability, readability, and reliability.",
            category="code-quality",
            inputs=["code", "goal"],
            output="Refactored code and rationale",
        ),
        SkillDefinition(
            name="frontend-design",
            description="Generate polished frontend UI components, screens, and interfaces.",
            category="frontend",
            inputs=["design_goal", "stack"],
            output="Design and implementation guidance",
        ),
        SkillDefinition(
            name="web-design-reviewer",
            description="Review UI designs for responsiveness, spacing, accessibility, and consistency.",
            category="frontend",
            inputs=["description_or_screenshot", "users"],
            output="Review findings and fixes",
        ),
        SkillDefinition(
            name="diagram-generator",
            description="Generate architecture diagrams and system flowcharts from descriptions.",
            category="architecture",
            inputs=["system_description"],
            output="Mermaid or structured diagram output",
        ),
        SkillDefinition(
            name="webapp-testing",
            description="Design browser-based tests for web application workflows.",
            category="testing",
            inputs=["feature", "environment"],
            output="Validation plan and test notes",
        ),
        SkillDefinition(
            name="code-change-verification",
            description="Verify that a code change is complete, correct, and safe to merge.",
            category="quality-assurance",
            inputs=["change_summary", "repo_context"],
            output="Verification checklist and risks",
        ),
        SkillDefinition(
            name="mcp-builder",
            description="Build and document Model Context Protocol integrations with APIs and services.",
            category="integration",
            inputs=["service", "requirements"],
            output="MCP design and implementation guidance",
        ),
        SkillDefinition(
            name="repo-contribution",
            description="Guide repository contribution steps for clean commits and PR-ready work.",
            category="workflow",
            inputs=["task", "repository"],
            output="Contribution flow and pull request checklist",
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
        "1. Clarify scope and constraints.\n"
        "2. Produce the relevant implementation or analysis.\n"
        "3. Validate quality through tests or review.\n"
        "4. Summarize trade-offs and next steps."
    )


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Development skill catalog")
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
