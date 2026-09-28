from marketing_skill.skill import get_skill_catalog, run_skill


def test_catalog_has_marketing_skills():
    names = {item.name for item in get_skill_catalog()}
    assert "campaign-planner" in names
    assert "seo-audit" in names


def test_run_skill_returns_data():
    result = run_skill("audience-segmentation", "Segment users by lifecycle stage.")
    assert "Skill: audience-segmentation" in result
