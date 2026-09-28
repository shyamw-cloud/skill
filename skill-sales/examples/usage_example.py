from sales_skill.skill import get_skill_catalog, run_skill

if __name__ == "__main__":
    print("Available sales skills:")
    for skill in get_skill_catalog():
        print(f"- {skill.name}: {skill.description}")
    print("\nExample:")
    print(run_skill("sales-forecast", "Forecast Q4 revenue for a B2B SaaS team."))
