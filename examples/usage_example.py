"""Development skill pack for Smithery-compatible workflows.

This module exposes a lightweight catalog of development-related skills that can be
used as the basis for a larger Smithery skill package. It is intentionally
simple and dependency-light so it can be extended without additional setup.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Dict, List


@dataclass(frozen=True)
class SkillDefinition:
    """Metadata for a single development skill."""

    name: str
    description: str
    category: str
    inputs: List[str]
    output: str


def get_skill_catalog() -> List[SkillDefinition]:
    """Return the packaged development skill catalog."""

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
            description="Generate polished frontend UX, components, and layouts for web apps.",
            category="frontend",
            inputs=["design_goal", "tech_stack"],
            output="UI/component plan and implementation guidance",
        ),
        SkillDefinition(
            name="web-design-reviewer",
            description="Review web interfaces for accessibility, responsiveness, and consistency.",
            category="frontend",
            inputs=["screenshot_or_description", "target_users"],
            output="Review findings and fixes",
        ),
        SkillDefinition(
            name="diagram-generator",
            description="Generate architecture and workflow diagrams from natural-language system descriptions.",
            category="architecture",
            inputs=["system_description"],
            output="Diagram specification or Mermaid flowchart",
        ),
        SkillDefinition(
            name="webapp-testing",
            description="Define and run browser-based verification tasks for web app behavior.",
            category="testing",
            inputs=["feature", "test_target"],
            output="Test plan and validation notes",
        ),
        SkillDefinition(
            name="code-change-verification",
            description="Verify whether a code change satisfies the intended task and is safe to ship.",
            category="quality-assurance",
            inputs=["change_summary", "repo_context"],
            output="Verification checklist and risks",
        ),
        SkillDefinition(
            name="mcp-builder",
            description="Design or implement a Model Context Protocol server for external APIs or services.",
            category="integration",
            inputs=["service_context", "protocol_requirements"],
            output="MCP server design and implementation guidance",
        ),
        SkillDefinition(
            name="repo-contribution",
            description="Prepare repository contribution steps including issue work, commit quality, and PR hygiene.",
            category="automation",
            inputs=["task", "repo_context"],
            output="Contribution workflow and PR guidance",
        ),
    ]


def run_skill(skill_name: str, prompt: str) -> str:
    """Return a simple, deterministic template response for a requested skill.

    This intentionally keeps the implementation lightweight while still making the
    repo useful as a starting point for real Smithery integrations.
    """

    catalog = {item.name: item for item in get_skill_catalog()}
    skill = catalog.get(skill_name)

    if skill is None:
        available = ", ".join(sorted(catalog))
        return (
            f"Unknown skill '{skill_name}'. Available skills: {available}. "
            "Choose one of the packaged development skills."
        )

    return (
        f"Skill: {skill.name}\n"
        f"Category: {skill.category}\n"
        f"Description: {skill.description}\n\n"
        f"Request context:\n{prompt}\n\n"
        "Recommended execution plan:\n"
        "1. Clarify scope and target stack.\n"
        "2. Define the exact inputs required for this task.\n"
        "3. Produce the implementation or verification artifact.\n"
        "4. Validate against tests, linting, or runtime checks.\n"
        "5. Summarize trade-offs and next steps."
    )


def _build_parser() -> None:
    """Simple CLI entrypoint for local testing."""

    import argparse

    parser = argparse.ArgumentParser(description="Development skill pack")
    parser.add_argument("--list", action="store_true", help="List available skills")
    parser.add_argument("--skill", help="Name of a skill to run")
    parser.add_argument("--prompt", help="Prompt or task description to send to the skill")
    args = parser.parse_args()

    if args.list:
        for skill in get_skill_catalog():
            print(f"- {skill.name}: {skill.description}")
        return

    if args.skill:
        prompt = args.prompt or "No prompt provided."
        print(run_skill(args.skill, prompt))
        return

    parser.print_help()


if __name__ == "__main__":
    _build_parser()
