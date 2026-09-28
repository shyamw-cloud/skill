from operations_skill.skill import get_skill_catalog, run_skill


def test_catalog_has_operations_skills():
    names = {item.name for item in get_skill_catalog()}
    assert "process-mapping" in names
    assert "capacity-analysis" in names


def test_run_skill_returns_data():
    result = run_skill("resource-planning", "Plan staffing for a quarterly rollout.")
    assert "Skill: resource-planning" in result
