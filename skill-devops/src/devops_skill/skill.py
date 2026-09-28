"""DevOps skill catalog."""

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
        SkillDefinition("docker-setup", "Design a Docker-based runtime configuration for an application.", "devops", ["app_type", "runtime"], "Docker plan"),
        SkillDefinition("ci-cd-builder", "Create a CI/CD pipeline strategy for automated delivery.", "devops", ["repo", "deployment_targets"], "Pipeline design"),
        SkillDefinition("kubernetes-ops", "Plan Kubernetes deployment, scaling, and rollout practices.", "kubernetes", ["service", "environment"], "Kubernetes plan"),
        SkillDefinition("cloud-cost-optimizer", "Identify cloud spend issues and optimization opportunities.", "cloud", ["usage_data", "constraints"], "Cost optimization plan"),
        SkillDefinition("deployment-checklist", "Generate release and rollback checklists for product deployments.", "operations", ["release", "environment"], "Deployment checklist"),
        SkillDefinition("infra-health-review", "Assess the operational health of infrastructure and delivery pipelines.", "monitoring", ["infra_data", "alerts"], "Health review"),
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
        "Recommended steps:\n1. Define the environment and deployment target\n2. Identify operational constraints\n3. Produce setup or rollout plan\n4. Include rollback and monitoring guidance"
    )


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="DevOps skill pack")
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
