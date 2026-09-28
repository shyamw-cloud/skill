from customer_success_skill.skill import get_skill_catalog, run_skill


def test_catalog_has_customer_success_skills():
    names = {item.name for item in get_skill_catalog()}
    assert "customer-health-score" in names
    assert "renewal-risk-analyzer" in names


def test_run_skill_returns_data():
    result = run_skill("onboarding-roadmap", "Create an onboarding roadmap for a new implementation customer.")
    assert "Skill: onboarding-roadmap" in result
