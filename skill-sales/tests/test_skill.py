from sales_skill.skill import get_skill_catalog, run_skill


def test_catalog_has_sales_skills():
    names = {item.name for item in get_skill_catalog()}
    assert "lead-prioritization" in names
    assert "proposal-generator" in names


def test_run_skill_returns_data():
    result = run_skill("pipeline-review", "Review the current pipeline quality.")
    assert "Skill: pipeline-review" in result
