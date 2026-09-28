from finance_skill.skill import get_skill_catalog, run_skill

if __name__ == "__main__":
    print("Available finance skills:")
    for skill in get_skill_catalog():
        print(f"- {skill.name}: {skill.description}")
    print("\nExample:")
    print(run_skill("budget-analysis", "Compare the Q3 budget against actuals and summarize variances."))
