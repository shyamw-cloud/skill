from devops_skill.skill import get_skill_catalog, run_skill


def test_catalog_has_devops_skills():
    names = {item.name for item in get_skill_catalog()}
    assert "docker-setup" in names
    assert "cloud-cost-optimizer" in names


def test_run_skill_returns_data():
    result = run_skill("deployment-checklist", "Build a release checklist for a customer-facing service.")
    assert "Skill: deployment-checklist" in result
