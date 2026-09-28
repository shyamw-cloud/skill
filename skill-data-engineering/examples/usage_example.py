from data_engineering_skill.skill import get_skill_catalog, run_skill

if __name__ == "__main__":
    print("Available data engineering skills:")
    for skill in get_skill_catalog():
        print(f"- {skill.name}: {skill.description}")
    print("\nExample:")
    print(run_skill("etl-design", "Design an ETL flow for sales and product usage events."))
