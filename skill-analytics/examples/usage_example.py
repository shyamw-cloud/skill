from analytics_skill.skill import get_skill_catalog, run_skill

if __name__ == "__main__":
    print("Available analytics skills:")
    for skill in get_skill_catalog():
        print(f"- {skill.name}: {skill.description}")
    print("\nExample:")
    print(run_skill("kpi-reporting", "Report on Q3 sales and retention metrics."))
