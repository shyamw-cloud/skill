from security_skill.skill import get_skill_catalog, run_skill


def test_catalog_has_security_skills():
    names = {item.name for item in get_skill_catalog()}
    assert "threat-modeling" in names
    assert "policy-compliance-check" in names


def test_run_skill_returns_data():
    result = run_skill("privacy-risk-assessment", "Review data handling for a new feature.")
    assert "Skill: privacy-risk-assessment" in result
