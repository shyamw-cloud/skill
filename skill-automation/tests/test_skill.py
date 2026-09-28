from automation_skill.skill import get_skill_catalog, run_skill


def test_catalog_has_automation_skills():
    names = {item.name for item in get_skill_catalog()}
    assert "workflow-automation" in names
    assert "approval-router" in names


def test_run_skill_returns_data():
    result = run_skill("notification-engine", "Notify teams when SLA breaches occur.")
    assert "Skill: notification-engine" in result
