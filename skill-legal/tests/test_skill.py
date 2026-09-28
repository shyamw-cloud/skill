from legal_skill.skill import get_skill_catalog, run_skill


def test_catalog_has_legal_skills():
    names = {item.name for item in get_skill_catalog()}
    assert "contract-review" in names
    assert "regulatory-mapping" in names


def test_run_skill_returns_data():
    result = run_skill("policy-extraction", "Extract obligations from a privacy document.")
    assert "Skill: policy-extraction" in result
