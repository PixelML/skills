# AgenticFlow CLI Reference

The `agenticflow` CLI is the primary interface for interacting with AgenticFlow from the command line. It replaces MCP tool calls with direct CLI commands.

## Prerequisites

```bash
# Install (npm)
npm install -g @pixelml/agenticflow-cli

# Authenticate
agenticflow login

# Verify setup
agenticflow doctor --json
```

## Command Mapping (MCP → CLI)

| MCP Tool | CLI Command |
|----------|-------------|
| `agenticflow_list_node_types` | `agenticflow node-types list` |
| `agenticflow_search_node_types` | `agenticflow node-types search --query <q>` |
| `agenticflow_get_node_type_details` | `agenticflow node-types get --name <name>` |
| `agenticflow_get_dynamic_options` | `agenticflow node-types dynamic-options --name <node> --field-name <field>` |
| `agenticflow_create_workflow` | `agenticflow workflow create --body @workflow.json` |
| `agenticflow_update_workflow` | `agenticflow workflow update --workflow-id <id> --body @workflow.json` |
| `agenticflow_execute_workflow` | `agenticflow workflow run --workflow-id <id> --input @input.json` |
| `agenticflow_get_workflow_run` | `agenticflow workflow run-status --workflow-run-id <id>` |
| `agenticflow_list_workflows` | `agenticflow workflow list` |
| `agenticflow_get_workflow_details` | `agenticflow workflow get --workflow-id <id>` |
| `agenticflow_list_app_connections` | `agenticflow connections list` |
| `agenticflow_list_agents` | `agenticflow agent list` |
| `agenticflow_create_agent` | `agenticflow agent create --body @agent.json` |
| `agenticflow_update_agent` | `agenticflow agent update --agent-id <id> --body @agent.json` |
| `agenticflow_get_agent_details` | `agenticflow agent get --agent-id <id>` |

## Common Patterns

### JSON output
All commands support `--json` for machine-readable output.

### File input
Use `@path/to/file.json` to pass JSON from a file:
```bash
agenticflow workflow create --body @workflow.json
agenticflow workflow run --workflow-id <id> --input @input.json
```

### Dry run
Preview what would be sent without executing:
```bash
agenticflow workflow create --body @workflow.json --dry-run
```

### Low-level call (fallback)
For any operation, use `call` with the operation ID:
```bash
# List node types (fallback if high-level command fails)
agenticflow call --operation-id get_nodetype_models_v1_node_types__get --json

# Get node type by name
agenticflow call --operation-id get_nodetype_model_by_name_v1_node_types_name__name__get \
  --path-param name=generate_image --json
```

### Discover operations
```bash
agenticflow ops list --public-only
agenticflow ops show <operation-id>
```

## Workflow Lifecycle

```bash
# 1. Discover node types
agenticflow node-types search --query "image"

# 2. Validate workflow definition
agenticflow workflow validate --body @workflow.json

# 3. Create workflow
agenticflow workflow create --body @workflow.json

# 4. Run workflow
agenticflow workflow run --workflow-id <id> --input @input.json

# 5. Check status
agenticflow workflow run-status --workflow-run-id <run-id>
```

## Agent Lifecycle

```bash
# 1. Create agent
agenticflow agent create --body @agent.json

# 2. Interact via streaming
agenticflow agent stream --agent-id <id> --body @stream.json

# 3. Update agent
agenticflow agent update --agent-id <id> --body @agent.json
```
