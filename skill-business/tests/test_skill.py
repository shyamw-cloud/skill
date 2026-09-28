from business_skill.skill import get_skill_catalog, run_skill


def test_catalog_contains_expected_skills():
    names = {item.name for item in get_skill_catalog()}
    assert "business-analytics" in names
    assert "sales-forecasting" in names
    assert "crm-automation" in names
    assert "inventory-forecasting" in names


def test_run_skill_returns_content():
    result = run_skill("business-analytics", "Analyze Q4 revenue trends.")
    assert "Skill: business-analytics" in result
    assert "Recommended process" in result
