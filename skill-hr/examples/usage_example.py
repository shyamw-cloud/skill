from hr_skill.skill import get_skill_catalog, run_skill

if __name__ == "__main__":
    print("Available HR skills:")
    for skill in get_skill_catalog():
        print(f"- {skill.name}: {skill.description}")
    print("\nExample:")
    print(run_skill("hiring-assistant", "Recruit for a senior frontend engineer role."))
