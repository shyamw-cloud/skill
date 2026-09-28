from data_engineering_skill.skill import get_skill_catalog, run_skill


def test_catalog_has_data_engineering_skills():
    names = {item.name for item in get_skill_catalog()}
    assert "data-pipeline-builder" in names
    assert "schema-designer" in names


def test_run_skill_returns_data():
    result = run_skill("data-quality-audit", "Audit missing and invalid records in a sales dataset.")
    assert "Skill: data-quality-audit" in result
