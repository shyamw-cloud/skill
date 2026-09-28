from security_skill.skill import get_skill_catalog, run_skill

if __name__ == "__main__":
    print("Available security skills:")
    for skill in get_skill_catalog():
        print(f"- {skill.name}: {skill.description}")
    print("\nExample:")
    print(run_skill("access-audit", "Audit role permissions across the support and admin tools."))
