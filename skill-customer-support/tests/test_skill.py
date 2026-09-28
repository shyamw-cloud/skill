from support_skill.skill import get_skill_catalog, run_skill


def test_catalog_has_support_skills():
    names = {item.name for item in get_skill_catalog()}
    assert "ticket-triage" in names
    assert "response-drafter" in names


def test_run_skill_returns_data():
    result = run_skill("helpdesk-automation", "Route onboarding and billing issues to the correct team.")
    assert "Skill: helpdesk-automation" in result
