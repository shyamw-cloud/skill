from analytics_skill.skill import get_skill_catalog, run_skill


def test_catalog_has_analytics_skills():
    names = {item.name for item in get_skill_catalog()}
    assert "kpi-reporting" in names
    assert "anomaly-detector" in names


def test_run_skill_returns_data():
    result = run_skill("trend-analysis", "Review monthly demand data.")
    assert "Skill: trend-analysis" in result
