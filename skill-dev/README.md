# Development Skill Pack

A Smithery-ready collection of practical development and engineering skills for coding, testing, UI design, architecture, and repo automation.

## Overview

This package contains common developer-focused AI skills that help with software delivery and engineering productivity.

## Included Skills

- `refactor` — improve maintainability and code quality
- `frontend-design` — design polished React/UI components and screens
- `web-design-reviewer` — review responsiveness, layout, and accessibility
- `diagram-generator` — generate architecture diagrams and flow charts
- `webapp-testing` — create or validate browser-based app behavior
- `code-change-verification` — verify the safety and completeness of code changes
- `mcp-builder` — build MCP tools and integrations
- `repo-contribution` — prepare issues, commit messages, and PR workflows

## Folder Structure

```text
development-skill/
├── README.md
├── smithery.yaml
├── requirements.txt
├── pyproject.toml
├── .gitignore
├── src/
│   └── dev_skill/
│       ├── __init__.py
│       └── skill.py
├── examples/
│   └── usage_example.py
├── tests/
│   └── test_skill.py
└── LICENSE
```

## Quick Start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m dev_skill --list
```

## Example

```bash
python -m dev_skill --skill refactor --prompt "Extract reusable validation logic in a Python service."
```

## License

MIT
