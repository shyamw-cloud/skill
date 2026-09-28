from marketing_skill.skill import get_skill_catalog, run_skill

if __name__ == "__main__":
    print("Available marketing skills:")
    for skill in get_skill_catalog():
        print(f"- {skill.name}: {skill.description}")
    print("\nExample:")
    print(run_skill("campaign-planner", "Plan a Q4 B2B campaign for software buyers."))
