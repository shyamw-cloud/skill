# Development Skill Pack

This repository is a Smithery-ready development skill pack for coding workflows, frontend work, testing, architecture, and tool integration.

It includes a modular Python package with a catalog of development-focused skills inspired by the Smithery.ai ecosystem:

- Code refactoring
- Frontend design
- UI review
- Architecture diagram generation
- Web testing and verification
- MCP server/tool integration
- Repository contribution workflows

## Repository structure

```text
.
├── README.md
├── smithery.yaml
├── requirements.txt
├── pyproject.toml
├── .gitignore
├── src/
│   └── skill/
│       ├── __init__.py
│       └── skill.py
├── examples/
│   └── usage_example.py
├── tests/
│   └── test_skill.py
└── LICENSE
```

## Quick start

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m skill.skill --help
```

## Included skill catalog

- `refactor`: improves maintainability and readability
- `frontend-design`: creates polished React or UI components
- `web-design-reviewer`: checks responsive design and accessibility
- `diagram-generator`: creates architecture/flow diagrams
- `webapp-testing`: validates frontend behavior with browser automation
- `code-change-verification`: checks whether code changes are safe and complete
- `mcp-builder`: guides building MCP servers and integrations
- `repo-contribution`: helps with PR discipline and repo workflows

## Smithery packaging

The project includes a `smithery.yaml` manifest so it can be used as a Smithery skill package or adapted into a more specialized package.

## License

MIT
