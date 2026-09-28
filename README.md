# Smithery Skill Repository

A modular collection of Smithery-ready skill packs organized by category. This repository is designed to serve as an extensible library of AI-powered skills for business, engineering, operations, product, and AI orchestration workflows.

## Overview

This repo contains multiple category-based skill packs. Each skill pack is a self-contained Python package with its own README, metadata, example usage, and tests. The goal is to make it easy to add, browse, and extend skills for different business and technical use cases.

## Skill Categories

### 1. Development
Directory: `skill-dev`

Core skills:
- refactor
- frontend-design
- web-design-reviewer
- diagram-generator
- webapp-testing
- code-change-verification
- mcp-builder
- repo-contribution

### 2. Business
Directory: `skill-business`

Core skills:
- business-analytics
- sales-forecasting
- crm-automation
- financial-analysis
- document-extraction
- workflow-optimization
- sentiment-analysis
- inventory-forecasting

### 3. Analytics
Directory: `skill-analytics`

Core skills:
- dashboard-analysis
- trend-analysis
- anomaly-detector
- kpi-reporting
- executive-summary
- market-insight-generator

### 4. Marketing
Directory: `skill-marketing`

Core skills:
- campaign-planner
- content-strategy
- seo-audit
- audience-segmentation
- brand-positioning
- lead-nurture-planner

### 5. Sales
Directory: `skill-sales`

Core skills:
- lead-prioritization
- sales-forecast
- proposal-generator
- pipeline-review
- renewal-risk-analyzer
- sales-enablement

### 6. HR
Directory: `skill-hr`

Core skills:
- hiring-assistant
- onboarding-planner
- performance-review-analyzer
- employee-engagement-insights
- talent-pipeline-review
- policy-clarifier

### 7. Customer Support
Directory: `skill-customer-support`

Core skills:
- ticket-triage
- helpdesk-automation
- response-drafter
- issue-resolution-guide
- feedback-classifier
- customer-health-summary

### 8. Automation
Directory: `skill-automation`

Core skills:
- workflow-automation
- approval-router
- notification-engine
- task-scheduler
- document-routing
- integration-orchestrator

### 9. Operations
Directory: `skill-operations`

Core skills:
- process-mapping
- resource-planning
- vendor-management
- capacity-analysis
- service-level-review
- incident-prioritization

### 10. AI Agent
Directory: `skill-ai-agent`

Core skills:
- prompt-optimizer
- tool-router
- multi-agent-planner
- workflow-coordinator
- knowledge-base-curator
- reasoning-assistant

### 11. Security & Compliance
Directory: `skill-security`

Core skills:
- threat-modeling
- vulnerability-review
- secure-code-checker
- access-audit
- privacy-risk-assessment
- policy-compliance-check

### 12. Product & Strategy
Directory: `skill-product`

Core skills:
- roadmap-builder
- feature-prioritizer
- competitive-analysis
- pricing-strategy
- customer-interview-summarizer
- decision-support-assistant

---

## Repository Structure

```text
skill/
├── README.md
├── LICENSE
├── skill-dev/
├── skill-business/
├── skill-analytics/
├── skill-marketing/
├── skill-sales/
├── skill-hr/
├── skill-customer-support/
├── skill-automation/
├── skill-operations/
├── skill-ai-agent/
├── skill-security/
├── skill-product/
└── .github/
    └── workflows/
        └── ci.yml
```

---

## How to Use

Each directory is a standalone skill pack. You can run or test any pack individually.

Example:

```bash
cd skill-dev
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m dev_skill --list
```

Or:

```bash
cd skill-business
python -m business_skill --list
```

---

## Future Expansion

This repository can be extended with more domain packs such as:
- Finance
- Legal
- Procurement
- DevOps/Cloud
- Data Engineering
- Customer Success
- AI Safety
- Education
- Healthcare

---

## License

MIT License
