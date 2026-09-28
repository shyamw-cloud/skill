from product_skill.skill import get_skill_catalog, run_skill


def test_catalog_has_product_skills():
    names = {item.name for item in get_skill_catalog()}
    assert "roadmap-builder" in names
    assert "competitive-analysis" in names


def test_run_skill_returns_data():
    result = run_skill("feature-prioritizer", "Prioritize features for the next release.")
    assert "Skill: feature-prioritizer" in result
