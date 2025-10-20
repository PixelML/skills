---
name: notebooklm
description: Use this skill to query your Google NotebookLM notebooks directly from Claude Code for source-grounded, citation-backed answers from Gemini. Browser automation, library management, persistent auth. Drastically reduced hallucinations through document-only responses.
license: Complete terms in LICENSE.txt
allowed-tools:
  - Bash
  - Read
  - Write
  - Edit
  - Glob
  - Grep
---

# NotebookLM Research Assistant

Query Google NotebookLM notebooks for source-grounded, citation-backed answers from Gemini. Each query opens a fresh browser session, retrieves answers exclusively from uploaded documents, and closes.

## Decision Tree: Workflow Selection

```
User request → Is it about NotebookLM?
    ├─ Yes → What type of request?
    │    ├─ Authentication → Run setup_notebooklm.py
    │    ├─ Add notebook → Smart discovery or manual add
    │    ├─ Ask question → Quick query or library query
    │    └─ Manage library → List, search, activate, remove
    │
    └─ No → Do not use this skill
```

## Quick Start

### Step 1: One-Time Setup
Run the automated setup script:
```bash
python scripts/setup_notebooklm.py
```

This handles:
- Authentication setup (opens browser for Google login)
- Virtual environment creation
- Dependency installation

### Step 2: Query Notebooks

**Quick Query (recommended):**
```bash
python scripts/quick_query.py "Your question here" --url "https://notebooklm.google.com/notebook/..."
```

**Library Query:**
```bash
# First add notebook to library
python scripts/run.py notebook_manager.py add --url "URL" --name "Name" --description "Description" --topics "topics"

# Then query
python scripts/run.py ask_question.py --question "Your question"
```

## Core Workflows

### Workflow 1: One-Time Questions
For quick, one-off queries without library management:

```bash
python scripts/quick_query.py "What are the key findings?" --url "https://notebooklm.google.com/notebook/..."
```

### Workflow 2: Smart Discovery & Addition
Discover notebook content automatically before adding:

```bash
# Step 1: Discover content
python scripts/run.py ask_question.py \
  --question "What topics are covered? Provide overview" \
  --notebook-url "URL"

# Step 2: Add with discovered metadata
python scripts/run.py notebook_manager.py add \
  --url "URL" --name "Discovered Name" \
  --description "Auto-discovered description" \
  --topics "topic1,topic2,topic3"
```

### Workflow 3: Library Management
Build and manage a persistent notebook library:

```bash
# List all notebooks
python scripts/run.py notebook_manager.py list

# Search notebooks
python scripts/run.py notebook_manager.py search --query "machine learning"

# Set active notebook
python scripts/run.py notebook_manager.py activate --id notebook-id

# Ask questions about active notebook
python scripts/run.py ask_question.py --question "Explain the methodology"
```

## Helper Scripts (Black Box Usage)

Use these scripts as black boxes - don't read their source, just invoke them:

### `scripts/setup_notebooklm.py`
Automated one-time setup for authentication and environment.

### `scripts/quick_query.py`
Fast querying without library management:
```bash
python scripts/quick_query.py "question" [--url URL] [--show-browser]
```

### `scripts/run.py`
Universal wrapper for all operations:
```bash
python scripts/run.py <script> [args]
```

**Always use run.py wrapper** - handles environment automatically.

## Examples

### Example 1: Research Query
```bash
python scripts/quick_query.py "What are the economic benefits of SLMs?" --url "https://notebooklm.google.com/notebook/research-id"
```

### Example 2: Academic Paper Analysis
```bash
# Add paper to library
python scripts/run.py notebook_manager.py add \
  --url "paper-url" --name "AI Ethics Paper" \
  --description "Research on AI ethics and bias" \
  --topics "AI,ethics,bias,research"

# Query specific aspects
python scripts/run.py ask_question.py --question "What bias mitigation techniques are proposed?"
```

### Example 3: Business Intelligence
```bash
python scripts/quick_query.py "Summarize Q3 financial performance" --url "financial-reports-url"
```

## Reference Files

### `examples/basic_query.py`
Demonstrates the most common usage pattern - querying the active notebook.

### `examples/smart_add.py`
Shows smart discovery workflow - discover content before adding to library.

### `references/api_reference.md`
Complete API documentation for all scripts and parameters.

### `references/troubleshooting.md`
Common issues and solutions for authentication, browser, and network problems.

### `references/usage_patterns.md`
Advanced workflow examples and best practices for enterprise use cases.

## Best Practices

1. **Use helper scripts as black boxes** - Don't read their source, just invoke them
2. **Start with setup_notebooklm.py** for first-time users
3. **Use quick_query.py for one-off questions** - faster and simpler
4. **Build library for repeated queries** - more efficient for ongoing work
5. **Smart discovery over manual metadata** - let AI discover content details
6. **Always check authentication status** if queries fail

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Authentication fails | Run `python scripts/setup_notebooklm.py` |
| Browser won't open | Use `--show-browser` flag |
| Rate limit (50/day) | Wait or switch Google account |
| Empty answers | Check notebook URL and authentication |

## Integration Notes

- **Claude Code**: Current setup with scripts and helper tools
- **Claude API**: Skills endpoint with the same functionality
- **Claude.ai**: Web interface with automatic skill loading

The skill maintains a clean separation between core instructions (SKILL.md) and detailed reference materials, enabling progressive disclosure based on task complexity.