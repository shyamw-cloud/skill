from hr_skill.skill import get_skill_catalog, run_skill


def test_catalog_has_hr_skills():
    names = {item.name for item in get_skill_catalog()}
    assert "hiring-assistant" in names
    assert "policy-clarifier" in names


def test_run_skill_returns_data():
    result = run_skill("onboarding-planner", "Create an onboarding plan for a new product manager.")
    assert "Skill: onboarding-planner" in result
