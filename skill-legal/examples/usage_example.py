from legal_skill.skill import get_skill_catalog, run_skill

if __name__ == "__main__":
    print("Available legal skills:")
    for skill in get_skill_catalog():
        print(f"- {skill.name}: {skill.description}")
    print("\nExample:")
    print(run_skill("contract-review", "Review a SaaS vendor agreement for key risks and obligations."))
