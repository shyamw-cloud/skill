from ai_agent_skill.skill import get_skill_catalog, run_skill

if __name__ == "__main__":
    print("Available AI agent skills:")
    for skill in get_skill_catalog():
        print(f"- {skill.name}: {skill.description}")
    print("\nExample:")
    print(run_skill("tool-router", "Route a bug-fix task to the right internal tools and workflow."))
