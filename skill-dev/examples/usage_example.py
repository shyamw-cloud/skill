import sys

from dev_skill.skill import get_skill_catalog, run_skill


if __name__ == "__main__":
    skills = get_skill_catalog()
    print("Available development skills:")
    for skill in skills:
        print(f"- {skill.name}: {skill.description}")

    print("\nExample:")
    print(run_skill("refactor", "Extract a reusable validation function for a Python API service."))
