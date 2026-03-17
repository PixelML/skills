---
name: image-gen
description: AI image generation via AgenticFlow cloud workflows or local API providers. Supports text-to-image, reference images, aspect ratios, and batch generation. AgenticFlow mode requires no API keys. Local mode supports OpenAI, Google, OpenRouter, DashScope, Jimeng, Seedream, and Replicate. Use when user asks to generate, create, or draw images.
license: MIT
allowed-tools:
  - Bash(agenticflow *)
  - Bash(bun *)
  - Bash(npx *)
  - Bash(curl *)
---

# Image Generation

Two execution modes:
- **AgenticFlow mode** (default) — cloud-based, no API keys needed, uses AgenticFlow workflows
- **Local mode** — direct API calls via TypeScript scripts, requires provider API keys

## Mode Selection

| Condition | Mode |
|-----------|------|
| `agenticflow doctor` succeeds (CLI installed + authenticated) | **AgenticFlow** |
| User has `EXTEND.md` with `mode: local` | **Local** |
| User explicitly asks for a specific local provider (e.g., "use OpenAI") | **Local** |
| No agenticflow CLI and no API keys | Prompt user to set up one of the two |

---

# AgenticFlow Mode

Uses AgenticFlow workflows with the `generate_image` or `agenticflow_generate_image` node type for cloud-based image generation.

## Step 0: Setup AgenticFlow Workflow

**0.1 Check CLI readiness**:
```bash
agenticflow doctor --json
```
If not authenticated → `agenticflow login`.

**0.2 Check EXTEND.md for saved workflow ID**:

```bash
test -f .agent-skills/image-gen/EXTEND.md && echo "project"
test -f "${XDG_CONFIG_HOME:-$HOME/.config}/agent-skills/image-gen/EXTEND.md" && echo "xdg"
test -f "$HOME/.agent-skills/image-gen/EXTEND.md" && echo "user"
```

If EXTEND.md has `agenticflow.workflow_id`, verify it:
```bash
agenticflow workflow get --workflow-id <saved_id> --json
```
If valid → use it. If error → continue to 0.3.

**0.3 Search for existing image generation workflow**:

```bash
agenticflow workflow list --json
```

Parse the JSON. Look for any workflow whose `nodes` array contains `node_type_name` equal to `"generate_image"` or `"agenticflow_generate_image"`. If found, store its `id` as `workflow_id`.

**0.4 No existing workflow → Create one**:

Check user's connections to decide node type:

```bash
agenticflow connections list --json
```

| Has `pixelml` connection? | Node type | Connection |
|--------------------------|-----------|------------|
| **Yes** | `generate_image` (Nano Banana 2, more providers) | `"{{__app_connections__['<pixelml_id>']}}"` |
| **No** | `agenticflow_generate_image` (built-in, zero setup) | `null` |

**Option A — With PixelML connection** (more providers, higher quality options):

```bash
cat > /tmp/af-imagegen-wf.json << 'WFEOF'
{
  "name": "Image Generator",
  "description": "Generates images from text prompts via AgenticFlow.",
  "input_schema": {
    "type": "object",
    "title": "User inputs",
    "required": ["prompt"],
    "properties": {
      "prompt": {
        "type": "string",
        "title": "Image Prompt",
        "ui_metadata": { "type": "long_text", "order": 0, "value": "", "placeholder": "Describe the image..." }
      }
    }
  },
  "nodes": {
    "nodes": [
      {
        "name": "generate_image",
        "title": "Generate Image",
        "node_type_name": "generate_image",
        "input_config": {
          "prompt": "{{prompt}}",
          "provider": "Nano Banana 2",
          "aspect_ratio": "16:9 (1K)",
          "negative_prompt": "NSFW, blurry, low quality, watermark",
          "model_id": null,
          "lora": null
        },
        "output_mapping": null,
        "connection": "{{__app_connections__['<PIXELML_CONNECTION_ID>']}}"
      }
    ]
  },
  "output_mapping": {}
}
WFEOF
```

Replace `<PIXELML_CONNECTION_ID>` with actual `id` from connections list where `category == "pixelml"`.

**Option B — Without connection** (works for any authenticated user):

```bash
cat > /tmp/af-imagegen-wf.json << 'WFEOF'
{
  "name": "Image Generator",
  "description": "Generates images from text prompts via AgenticFlow.",
  "input_schema": {
    "type": "object",
    "title": "User inputs",
    "required": ["prompt"],
    "properties": {
      "prompt": {
        "type": "string",
        "title": "Image Prompt",
        "ui_metadata": { "type": "long_text", "order": 0, "value": "", "placeholder": "Describe the image..." }
      }
    }
  },
  "nodes": {
    "nodes": [
      {
        "name": "generate_image",
        "title": "Generate Image",
        "node_type_name": "agenticflow_generate_image",
        "input_config": {
          "prompt": "{{prompt}}",
          "aspect_ratio": "16:9",
          "negative_prompt": "NSFW, blurry, low quality, watermark",
          "model": null,
          "format": null
        },
        "output_mapping": null,
        "connection": null
      }
    ]
  },
  "output_mapping": {}
}
WFEOF
```

**Create the workflow**:
```bash
agenticflow workflow create --body @/tmp/af-imagegen-wf.json --json
```

Save the returned `id` to EXTEND.md:
```yaml
agenticflow:
  workflow_id: "<returned_id>"
```

## AgenticFlow Usage

### Single Image

```bash
# 1. Write prompt to temp file
cat > /tmp/af-img-input.json << 'EOF'
{
  "prompt": "A serene mountain landscape at sunset, oil painting style"
}
EOF

# 2. Run workflow
agenticflow workflow run --workflow-id <workflow_id> --input @/tmp/af-img-input.json --json

# 3. Poll until complete (wait 3-5s between polls)
agenticflow workflow run-status --workflow-run-id <run_id> --json

# 4. Download image from output
curl -sL "<image_url_from_output>" -o output.png
```

The image URL is in `output.generate_image.image` or `state.nodes_state[0].output.image`.

### Sequential Multi-Image

For generating multiple images (e.g., for slide decks, comics, infographics):

1. For each prompt:
   a. Create input JSON with prompt text
   b. `agenticflow workflow run` → get `run_id`
   c. Poll `workflow run-status` until `success`
   d. Extract image URL → `curl` download
   e. Report progress: "Generated X/N"
2. Auto-retry once on failure per image

### Aspect Ratios (AgenticFlow)

**`generate_image` node** (with PixelML connection):

| Aspect Ratio | Value |
|--------------|-------|
| 16:9 (1K) | `"16:9 (1K)"` |
| 16:9 (2K) | `"16:9 (2K)"` |
| 9:16 (1K) | `"9:16 (1K)"` |
| 1:1 (1K) | `"1:1 (1K)"` |
| 4:3 (1K) | `"4:3 (1K)"` |

> Note: Exact options depend on the provider. Use `agenticflow node-types dynamic-options` to fetch current options if needed.

**`agenticflow_generate_image` node** (no connection):

| Aspect Ratio | Value |
|--------------|-------|
| 16:9 | `"16:9"` |
| 9:16 | `"9:16"` |
| 1:1 | `"1:1"` |
| 4:3 | `"4:3"` |

### Changing Provider/Aspect Ratio

To change the workflow's default provider or aspect ratio, update the workflow:

```bash
# Edit the JSON to change provider/aspect_ratio in input_config, then:
agenticflow workflow update --workflow-id <workflow_id> --body @/tmp/af-imagegen-wf.json --json
```

Available providers for `generate_image` node (with PixelML):
- `Nano Banana 2` (recommended)
- `Nano Banana Pro`
- `Runware`
- Other providers available via dynamic options

---

# Local Mode

Direct API-based image generation via TypeScript scripts. Requires provider API keys.

## Script Directory

**Agent Execution**:
1. `{baseDir}` = this SKILL.md file's directory
2. Script path = `{baseDir}/scripts/main.ts`
3. Resolve `${BUN_X}` runtime: if `bun` installed → `bun`; if `npx` available → `npx -y bun`; else suggest installing bun

## Step 0: Load Preferences

Check EXTEND.md existence (priority: project → user):

```bash
test -f .agent-skills/image-gen/EXTEND.md && echo "project"
test -f "${XDG_CONFIG_HOME:-$HOME/.config}/agent-skills/image-gen/EXTEND.md" && echo "xdg"
test -f "$HOME/.agent-skills/image-gen/EXTEND.md" && echo "user"
```

| Path | Location |
|------|----------|
| `.agent-skills/image-gen/EXTEND.md` | Project directory |
| `$HOME/.agent-skills/image-gen/EXTEND.md` | User home |

| Result | Action |
|--------|--------|
| Found | Load, parse, apply settings |
| Not found | Run first-time setup ([references/config/first-time-setup.md](references/config/first-time-setup.md)) → Save EXTEND.md |

**EXTEND.md Supports**: Default provider | Default quality | Default aspect ratio | Default image size | Default models | Batch worker cap | Provider-specific batch limits | AgenticFlow workflow_id | Mode (agenticflow/local)

Schema: `references/config/preferences-schema.md`

## Local Usage

```bash
# Basic
${BUN_X} {baseDir}/scripts/main.ts --prompt "A cat" --image cat.png

# With aspect ratio
${BUN_X} {baseDir}/scripts/main.ts --prompt "A landscape" --image out.png --ar 16:9

# High quality
${BUN_X} {baseDir}/scripts/main.ts --prompt "A cat" --image out.png --quality 2k

# From prompt files
${BUN_X} {baseDir}/scripts/main.ts --promptfiles system.md content.md --image out.png

# With reference images (Google, OpenAI, OpenRouter, or Replicate)
${BUN_X} {baseDir}/scripts/main.ts --prompt "Make blue" --image out.png --ref source.png

# Specific provider
${BUN_X} {baseDir}/scripts/main.ts --prompt "A cat" --image out.png --provider openai

# Batch mode
${BUN_X} {baseDir}/scripts/main.ts --batchfile batch.json
```

### Batch File Format

```json
{
  "jobs": 4,
  "tasks": [
    {
      "id": "hero",
      "promptFiles": ["prompts/hero.md"],
      "image": "out/hero.png",
      "provider": "replicate",
      "model": "google/nano-banana-pro",
      "ar": "16:9",
      "quality": "2k"
    }
  ]
}
```

## Local Options

| Option | Description |
|--------|-------------|
| `--prompt <text>`, `-p` | Prompt text |
| `--promptfiles <files...>` | Read prompt from files (concatenated) |
| `--image <path>` | Output image path |
| `--batchfile <path>` | JSON batch file for multi-image generation |
| `--jobs <count>` | Worker count for batch mode |
| `--provider` | `google\|openai\|openrouter\|dashscope\|jimeng\|seedream\|replicate` |
| `--model <id>`, `-m` | Model ID |
| `--ar <ratio>` | Aspect ratio (e.g., `16:9`, `1:1`) |
| `--size <WxH>` | Size (e.g., `1024x1024`) |
| `--quality normal\|2k` | Quality preset (default: `2k`) |
| `--imageSize 1K\|2K\|4K` | Image size for Google/OpenRouter |
| `--ref <files...>` | Reference images |
| `--n <count>` | Number of images |
| `--json` | JSON output |

## Environment Variables (Local Mode)

| Variable | Description |
|----------|-------------|
| `OPENAI_API_KEY` | OpenAI API key |
| `OPENROUTER_API_KEY` | OpenRouter API key |
| `GOOGLE_API_KEY` | Google API key |
| `DASHSCOPE_API_KEY` | DashScope API key |
| `REPLICATE_API_TOKEN` | Replicate API token |
| `JIMENG_ACCESS_KEY_ID` | Jimeng Volcengine access key |
| `JIMENG_SECRET_ACCESS_KEY` | Jimeng Volcengine secret key |
| `ARK_API_KEY` | Seedream Volcengine ARK API key |

## Provider Selection (Local Mode)

1. `--ref` provided + no `--provider` → auto-select Google → OpenAI → OpenRouter → Replicate
2. `--provider` specified → use it
3. Only one API key available → use that provider
4. Multiple available → default to Google

## Quality Presets (Local Mode)

| Preset | Google | OpenAI | OpenRouter | Replicate |
|--------|--------|--------|------------|-----------|
| `normal` | 1K | 1024px | 1K | 1K |
| `2k` (default) | 2K | 2048px | 2K | 2K |

## Model Resolution (Local Mode)

Priority: CLI `--model` > EXTEND.md `default_model.[provider]` > Env var `<PROVIDER>_IMAGE_MODEL` > Built-in default

### Key Models

| Provider | Default Model | Reference Image Support |
|----------|---------------|------------------------|
| Google | `gemini-3-pro-image-preview` | Yes |
| OpenAI | `gpt-image-1.5` | Yes |
| OpenRouter | `google/gemini-3.1-flash-image-preview` | Yes |
| DashScope | `qwen-image-2.0-pro` | No |
| Replicate | `google/nano-banana-pro` | Yes |
| Jimeng | `jimeng_t2i_v40` | No |
| Seedream | `doubao-seedream-5-0-260128` | No |

## Generation Mode (Local Mode)

| Mode | When to Use |
|------|-------------|
| Sequential (default) | Single images, small batches |
| Parallel batch (`--batchfile`) | 2+ tasks with saved prompt files |

## Error Handling

- Missing API key → error with setup instructions
- Generation failure → auto-retry up to 3 attempts
- Invalid aspect ratio → warning, proceed with default
- Reference images with unsupported provider → error with hint

## Extension Support

Custom configurations via EXTEND.md. See references/config/preferences-schema.md.

### EXTEND.md Schema (Combined)

```yaml
# Mode: agenticflow (default) or local
mode: agenticflow

# AgenticFlow settings
agenticflow:
  workflow_id: "<workflow-id>"
  provider: "Nano Banana 2"
  aspect_ratio: "16:9 (1K)"

# Local mode settings
default_provider: google
default_quality: 2k
default_ar: "16:9"
default_model:
  google: "gemini-3-pro-image-preview"
  openai: "gpt-image-1.5"
  openrouter: "google/gemini-3.1-flash-image-preview"
  replicate: "google/nano-banana-pro"
batch_max_workers: 10
```
