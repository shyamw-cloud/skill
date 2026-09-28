"""Security and compliance skill catalog."""

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
        SkillDefinition("threat-modeling", "Model likely security threats and attack paths for a system.", "security", ["architecture", "risks"], "Threat model"),
        SkillDefinition("vulnerability-review", "Review a system or code change for likely vulnerabilities.", "security", ["code_or_design", "context"], "Review checklist"),
        SkillDefinition("secure-code-checker", "Identify security weaknesses in implementation patterns.", "security", ["code", "environment"], "Secure coding feedback"),
        SkillDefinition("access-audit", "Review permissions and access patterns for risks or overexposure.", "governance", ["access_data", "roles"], "Access audit"),
        SkillDefinition("privacy-risk-assessment", "Assess privacy exposure and compliance risks for data handling.", "compliance", ["data_flows", "jurisdiction"], "Privacy risk assessment"),
        SkillDefinition("policy-compliance-check", "Check operations or code against policy and compliance expectations.", "compliance", ["policy", "implementation"], "Compliance checklist"),
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
        "Recommended steps:\n1. Identify assets and trust boundaries\n2. Review exposure points\n3. Summarize risks\n4. Recommend mitigations"
    )


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Security skill pack")
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
