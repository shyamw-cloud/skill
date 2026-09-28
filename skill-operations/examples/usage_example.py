from operations_skill.skill import get_skill_catalog, run_skill

if __name__ == "__main__":
    print("Available operations skills:")
    for skill in get_skill_catalog():
        print(f"- {skill.name}: {skill.description}")
    print("\nExample:")
    print(run_skill("process-mapping", "Map the support handoff process between teams."))
