---
name: skill-creator
description: Guide for creating effective Agent Skills for Claw. Use this skill when users want to create a new skill or update an existing skill that extends the agent's capabilities with specialized knowledge, workflows, or tool integrations.
license: MIT
compatibility: claw
---

# Skill Creator

This skill provides guidance for creating effective Agent Skills for Claw.

## About Skills

Skills are modular, self-contained packages that extend agent capabilities by providing specialized knowledge, workflows, and tools. Think of them as "onboarding guides" for specific domains or tasks—they transform Claw from a general-purpose agent into a specialized agent equipped with procedural knowledge.

### What Skills Provide

1. **Specialized workflows** - Multi-step procedures for specific domains
2. **Tool integrations** - Instructions for working with specific file formats or APIs
3. **Domain expertise** - Company-specific knowledge, schemas, business logic
4. **Bundled resources** - Scripts, references, and assets for complex and repetitive tasks

## Skill File Structure

Every skill consists of a required `SKILL.md` file and optional bundled resources:

```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter metadata (required)
│   │   ├── name: (required)
│   │   └── description: (required)
│   └── Markdown instructions (required)
└── Bundled Resources (optional)
    ├── scripts/          - Executable code (Python/Bash/etc.)
    ├── references/       - Documentation loaded into context as needed
    └── assets/           - Files used in output (templates, images, etc.)
```

## Skill Locations

Claw searches these locations for skills:

| Location | Path | Notes |
|----------|------|-------|
| **Global (User)** | `~/.claw/skill/<name>/SKILL.md` | User-installed skills |
| **Project** | `.claw/skill/<name>/SKILL.md` | Project-specific skills |
| **Claude-compatible** | `.claude/skills/<name>/SKILL.md` | For compatibility |

## SKILL.md Requirements

### Frontmatter (Required)

Each SKILL.md must start with YAML frontmatter:

```yaml
---
name: my-skill-name
description: Concise description of what this skill does and when to use it
license: MIT
compatibility: claw
---
```

**Required fields:**
- `name` - Must be lowercase, alphanumeric, with single hyphens (e.g., `git-release`, `pdf-editor`)
- `description` - 1-1024 characters, specific enough for the agent to choose correctly

**Optional fields:**
- `license` - License type
- `compatibility` - Set to `claw`
- `metadata` - Key-value pairs for custom metadata

### Name Validation Rules

The `name` field must:
- Be 1–64 characters
- Be lowercase alphanumeric with single hyphen separators
- Not start or end with `-`
- Not contain consecutive `--`
- Match the directory name that contains `SKILL.md`

Regex: `^[a-z0-9]+(-[a-z0-9]+)*$`

## Skill Creation Process

### Step 1: Understand the Use Case

Ask clarifying questions to understand what the skill should do:

- "What functionality should this skill support?"
- "What would a user say that should trigger this skill?"
- "Can you give examples of how this skill would be used?"

### Step 2: Plan the Skill Contents

Analyze each use case to identify what resources to include:

| Resource Type | When to Include | Example |
|---------------|-----------------|---------|
| **scripts/** | Deterministic code reused repeatedly | `scripts/rotate_pdf.py` |
| **references/** | Documentation loaded on-demand | `references/api_docs.md` |
| **assets/** | Templates and files for output | `assets/template.html` |

### Step 3: Create the Skill Directory

Create the skill in the user's global skills directory:

```bash
mkdir -p ~/.claw/skill/<skill-name>
```

Then create the `SKILL.md` file with proper frontmatter:

```bash
cat > ~/.claw/skill/<skill-name>/SKILL.md << 'EOF'
---
name: <skill-name>
description: <description of when and why to use this skill>
license: MIT
compatibility: claw
---

# <Skill Title>

<Brief overview of what the skill does>

## When to Use

<Clear guidance on when this skill applies>

## How to Use

<Step-by-step instructions for using the skill>
EOF
```

### Step 4: Write the Skill Content

When writing `SKILL.md`:

1. **Use imperative form** - Write "To accomplish X, do Y" rather than "You should"
2. **Be specific** - Include concrete examples and clear workflows
3. **Reference resources** - Document how to use any bundled scripts, references, or assets
4. **Keep it focused** - One skill should do one thing well

### Step 5: Test the Skill

After creating the skill:

1. Click **Refresh** in Agent Skills to reload the skill list
2. Verify the skill appears with correct name and description
3. Test by asking the agent to perform a task that should trigger the skill
4. Iterate based on results

## Best Practices

### Description Quality

The description determines when the agent uses the skill. Make it specific:

**Good:** "Create consistent GitHub releases with changelogs from merged PRs, version bumping, and `gh release create` command generation"

**Bad:** "Help with releases"

### Progressive Disclosure

Skills use a three-level loading system:

1. **Metadata** - Always in context (~100 words)
2. **SKILL.md body** - When skill triggers (<5k words recommended)
3. **Bundled resources** - Loaded on-demand (unlimited size)

Keep SKILL.md under 5k words. Move detailed documentation to `references/` files.

### File Organization

```
my-skill/
├── SKILL.md              # Core instructions (<5k words)
├── scripts/
│   └── helper.py         # Executable code
├── references/
│   └── api-docs.md       # Loaded when needed
└── assets/
    └── template.html     # Used in output
```

## Example: Simple Skill

```yaml
---
name: git-release
description: Create consistent releases and changelogs from merged PRs
license: MIT
compatibility: claw
---

# Git Release

## What This Skill Does

- Draft release notes from merged PRs
- Propose a version bump
- Generate a `gh release create` command

## When to Use

Use when preparing a tagged release. Ask clarifying questions if the versioning scheme is unclear.

## How to Use

1. Review recent merged PRs since last release
2. Categorize changes (features, fixes, docs)
3. Determine version bump (major/minor/patch)
4. Generate release notes and command
```
