from dev_skill.skill import get_skill_catalog, run_skill


def test_catalog_contains_expected_skills():
    names = {item.name for item in get_skill_catalog()}
    assert "refactor" in names
    assert "frontend-design" in names
    assert "webapp-testing" in names
    assert "repo-contribution" in names


def test_run_skill_returns_content():
    result = run_skill("refactor", "Improve maintainability for this service.")
    assert "Skill: refactor" in result
    assert "Recommended process" in result
