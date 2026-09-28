from product_skill.skill import get_skill_catalog, run_skill

if __name__ == "__main__":
    print("Available product and strategy skills:")
    for skill in get_skill_catalog():
        print(f"- {skill.name}: {skill.description}")
    print("\nExample:")
    print(run_skill("roadmap-builder", "Create a 12-month roadmap for a B2B SaaS product."))
