from procurement_skill.skill import get_skill_catalog, run_skill

if __name__ == "__main__":
    print("Available procurement skills:")
    for skill in get_skill_catalog():
        print(f"- {skill.name}: {skill.description}")
    print("\nExample:")
    print(run_skill("vendor-evaluation", "Evaluate vendors for a new cloud infrastructure requirement."))
