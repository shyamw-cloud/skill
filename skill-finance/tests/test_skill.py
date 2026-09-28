from finance_skill.skill import get_skill_catalog, run_skill


def test_catalog_has_finance_skills():
    names = {item.name for item in get_skill_catalog()}
    assert "budget-analysis" in names
    assert "roi-review" in names


def test_run_skill_returns_data():
    result = run_skill("cashflow-forecasting", "Forecast operating cash flow for the next quarter.")
    assert "Skill: cashflow-forecasting" in result
