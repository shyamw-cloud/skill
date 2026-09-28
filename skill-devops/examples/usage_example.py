from devops_skill.skill import get_skill_catalog, run_skill

if __name__ == "__main__":
    print("Available DevOps skills:")
    for skill in get_skill_catalog():
        print(f"- {skill.name}: {skill.description}")
    print("\nExample:")
    print(run_skill("ci-cd-builder", "Create a CI/CD strategy for a microservice deployment."))
