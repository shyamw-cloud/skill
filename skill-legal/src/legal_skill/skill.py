"""Legal skill catalog."""

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
        SkillDefinition("contract-review", "Summarize contract clauses and flag key legal risks.", "legal", ["contract", "jurisdiction"], "Contract review"),
        SkillDefinition("policy-extraction", "Extract obligations and rules from internal legal or policy documents.", "governance", ["document", "topic"], "Policy summary"),
        SkillDefinition("risk-due-diligence", "Assess risk exposure in a defined operational or business context.", "risk", ["context", "document_set"], "Risk brief"),
        SkillDefinition("legal-research-assistant", "Support research around legal questions, standards, and obligations.", "research", ["question", "jurisdiction"], "Research summary"),
        SkillDefinition("regulatory-mapping", "Map a process or product to relevant regulation and compliance needs.", "compliance", ["process", "jurisdiction"], "Regulatory mapping"),
        SkillDefinition("litigation-summary", "Summarize litigation materials, claims, and key facts for review.", "legal", ["case_material", "issue"], "Case summary"),
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
        "Recommended steps:\n1. Identify legal issue and jurisdiction\n2. Review relevant documents\n3. Summarize risks and obligations\n4. Recommend next legal action"
    )


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Legal skill pack")
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
