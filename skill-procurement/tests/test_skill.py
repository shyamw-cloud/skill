from procurement_skill.skill import get_skill_catalog, run_skill


def test_catalog_has_procurement_skills():
    names = {item.name for item in get_skill_catalog()}
    assert "vendor-evaluation" in names
    assert "supplier-risk-review" in names


def test_run_skill_returns_data():
    result = run_skill("sourcing-plan", "Create a sourcing plan for internal software tools.")
    assert "Skill: sourcing-plan" in result
