import sys

from business_skill.skill import get_skill_catalog, run_skill


if __name__ == "__main__":
    skills = get_skill_catalog()
    print("Available business skills:")
    for skill in skills:
        print(f"- {skill.name}: {skill.description}")

    print("\nExample:")
    print(run_skill("business-analytics", "Analyze Q3 KPI performance and flag weak operating areas."))
