import sys

from skill.skill import get_skill_catalog, run_skill


if __name__ == "__main__":
    skills = get_skill_catalog()
    print("Available skills:")
    for skill in skills:
        print(f"- {skill.name}: {skill.description}")

    print("\nExample run:")
    print(run_skill("refactor", "Extract a reusable helper for API timeout handling in a Python service."))
