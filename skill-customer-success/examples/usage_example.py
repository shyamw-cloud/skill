from customer_success_skill.skill import get_skill_catalog, run_skill

if __name__ == "__main__":
    print("Available customer success skills:")
    for skill in get_skill_catalog():
        print(f"- {skill.name}: {skill.description}")
    print("\nExample:")
    print(run_skill("customer-health-score", "Assess health for a mid-market enterprise customer."))
