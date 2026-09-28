from ai_agent_skill.skill import get_skill_catalog, run_skill


def test_catalog_has_ai_agent_skills():
    names = {item.name for item in get_skill_catalog()}
    assert "prompt-optimizer" in names
    assert "multi-agent-planner" in names


def test_run_skill_returns_data():
    result = run_skill("workflow-coordinator", "Coordinate a research and summarization workflow.")
    assert "Skill: workflow-coordinator" in result
