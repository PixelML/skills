---
name: slide-deck
description: Generates professional slide deck images from content. Creates outlines with style instructions, then generates individual slide images via AgenticFlow workflows. Use when user asks to "create slides", "make a presentation", "generate deck", "slide deck", or "PPT".
license: MIT
allowed-tools:
  - Bash(agenticflow *)
  - Bash(bun *)
  - Bash(npx *)
---

# Slide Deck Generator

Transform content into professional slide deck images. Uses **AgenticFlow** for high-quality image generation via cloud workflows.

## Usage

```bash
/slide-deck path/to/content.md
/slide-deck path/to/content.md --style sketch-notes
/slide-deck path/to/content.md --audience executives
/slide-deck path/to/content.md --lang zh
/slide-deck path/to/content.md --slides 10
/slide-deck path/to/content.md --outline-only
/slide-deck  # Then paste content
```

## Script Directory

**Agent Execution Instructions**:
1. Determine this SKILL.md file's directory path as `{baseDir}`
2. Script path = `{baseDir}/scripts/<script-name>.ts`
3. Resolve `${BUN_X}` runtime: if `bun` installed → `bun`; if `npx` available → `npx -y bun`; else suggest installing bun

| Script | Purpose |
|--------|---------|
| `scripts/merge-to-pptx.ts` | Merge slides into PowerPoint |
| `scripts/merge-to-pdf.ts` | Merge slides into PDF |

## Options

| Option | Description |
|--------|-------------|
| `--style <name>` | Visual style: preset name, `custom`, or custom style name |
| `--audience <type>` | Target: beginners, intermediate, experts, executives, general |
| `--lang <code>` | Output language (en, zh, ja, etc.) |
| `--slides <number>` | Target slide count (8-25 recommended, max 30) |
| `--outline-only` | Generate outline only, skip image generation |
| `--prompts-only` | Generate outline + prompts, skip images |
| `--images-only` | Generate images from existing prompts directory |
| `--regenerate <N>` | Regenerate specific slide(s): `--regenerate 3` or `--regenerate 2,5,8` |

**Slide Count by Content Length**:
| Content | Slides |
|---------|--------|
| < 1000 words | 5-10 |
| 1000-3000 words | 10-18 |
| 3000-5000 words | 15-25 |
| > 5000 words | 20-30 (consider splitting) |

## Style System

### Presets

| Preset | Dimensions | Best For |
|--------|------------|----------|
| `blueprint` (Default) | grid + cool + technical + balanced | Architecture, system design |
| `chalkboard` | organic + warm + handwritten + balanced | Education, tutorials |
| `corporate` | clean + professional + geometric + balanced | Investor decks, proposals |
| `minimal` | clean + neutral + geometric + minimal | Executive briefings |
| `sketch-notes` | organic + warm + handwritten + balanced | Educational, tutorials |
| `watercolor` | organic + warm + humanist + minimal | Lifestyle, wellness |
| `dark-atmospheric` | clean + dark + editorial + balanced | Entertainment, gaming |
| `notion` | clean + neutral + geometric + dense | Product demos, SaaS |
| `bold-editorial` | clean + vibrant + editorial + balanced | Product launches, keynotes |
| `editorial-infographic` | clean + cool + editorial + dense | Tech explainers, research |
| `fantasy-animation` | organic + vibrant + handwritten + minimal | Educational storytelling |
| `intuition-machine` | clean + cool + technical + dense | Technical docs, academic |
| `pixel-art` | pixel + vibrant + technical + balanced | Gaming, developer talks |
| `scientific` | clean + cool + technical + dense | Biology, chemistry, medical |
| `vector-illustration` | clean + vibrant + humanist + balanced | Creative, children's content |
| `vintage` | paper + warm + editorial + balanced | Historical, heritage |

### Style Dimensions

| Dimension | Options | Description |
|-----------|---------|-------------|
| **Texture** | clean, grid, organic, pixel, paper | Visual texture and background treatment |
| **Mood** | professional, warm, cool, vibrant, dark, neutral | Color temperature and palette style |
| **Typography** | geometric, humanist, handwritten, editorial, technical | Headline and body text styling |
| **Density** | minimal, balanced, dense | Information density per slide |

Full specs: `references/dimensions/*.md`

### Auto Style Selection

| Content Signals | Preset |
|-----------------|--------|
| tutorial, learn, education, guide, beginner | `sketch-notes` |
| classroom, teaching, school, chalkboard | `chalkboard` |
| architecture, system, data, analysis, technical | `blueprint` |
| creative, children, kids, cute | `vector-illustration` |
| briefing, academic, research, bilingual | `intuition-machine` |
| executive, minimal, clean, simple | `minimal` |
| saas, product, dashboard, metrics | `notion` |
| investor, quarterly, business, corporate | `corporate` |
| launch, marketing, keynote, magazine | `bold-editorial` |
| entertainment, music, gaming, atmospheric | `dark-atmospheric` |
| explainer, journalism, science communication | `editorial-infographic` |
| story, fantasy, animation, magical | `fantasy-animation` |
| gaming, retro, pixel, developer | `pixel-art` |
| biology, chemistry, medical, scientific | `scientific` |
| history, heritage, vintage, expedition | `vintage` |
| lifestyle, wellness, travel, artistic | `watercolor` |
| Default | `blueprint` |

## Design Philosophy

Decks designed for **reading and sharing**, not live presentation:
- Each slide self-explanatory without verbal commentary
- Logical flow when scrolling
- All necessary context within each slide
- Optimized for social media sharing

See `references/design-guidelines.md` for:
- Audience-specific principles
- Visual hierarchy
- Content density guidelines
- Color and typography selection
- Font recommendations

See `references/layouts.md` for layout options.

## File Management

### Output Directory

```
slide-deck/{topic-slug}/
├── source-{slug}.{ext}
├── outline.md
├── prompts/
│   └── 01-slide-cover.md, 02-slide-{slug}.md, ...
├── 01-slide-cover.png, 02-slide-{slug}.png, ...
├── {topic-slug}.pptx
└── {topic-slug}.pdf
```

**Slug**: Extract topic (2-4 words, kebab-case). Example: "Introduction to Machine Learning" → `intro-machine-learning`

**Conflict Handling**: See Step 1.3 for existing content detection and user options.

## Language Handling

**Detection Priority**:
1. `--lang` flag (explicit)
2. EXTEND.md `language` setting
3. User's conversation language (input language)
4. Source content language

**Rule**: ALL responses use user's preferred language:
- Questions and confirmations
- Progress reports
- Error messages
- Completion summaries

Technical terms (style names, file paths, code) remain in English.

## Workflow

Copy this checklist and check off items as you complete them:

```
Slide Deck Progress:
- [ ] Step 0: AgenticFlow setup (image generation workflow)
- [ ] Step 1: Setup & Analyze
  - [ ] 1.1 Load preferences
  - [ ] 1.2 Analyze content
  - [ ] 1.3 Check existing
- [ ] Step 2: Confirmation (Round 1, optional Round 2)
- [ ] Step 3: Generate outline
- [ ] Step 4: Review outline (conditional)
- [ ] Step 5: Generate prompts
- [ ] Step 6: Review prompts (conditional)
- [ ] Step 7: Generate images (via AgenticFlow)
- [ ] Step 8: Merge to PPTX/PDF
- [ ] Step 9: Output summary
```

### Flow

```
Input → AF Setup → Preferences → Analyze → [Check Existing?] → Confirm → Outline → [Review?] → Prompts → [Review?] → Images (AgenticFlow) → Merge → Complete
```

### Step 0: AgenticFlow Image Generation Setup

Before generating images, ensure an AgenticFlow image generation workflow exists. This step is **dynamic per user** — never hardcode workflow IDs.

**0.1 Check CLI readiness**:
```bash
agenticflow doctor --json
```
If not authenticated, run `agenticflow login` first.

**0.2 Check EXTEND.md for saved workflow ID**:

If EXTEND.md has `agenticflow.workflow_id`, verify it still exists:
```bash
agenticflow workflow get --workflow-id <saved_id> --json
```
If valid → use it, skip to Step 1. If 404/error → continue to 0.3.

**0.3 Search for existing image generation workflow**:

```bash
agenticflow workflow list --json
```

Parse the JSON output. Look for any workflow whose `nodes` array contains a node with `node_type_name` equal to `"generate_image"` or `"agenticflow_generate_image"`. If found, store its `id` as the `workflow_id` and skip to Step 1.

**0.4 No existing workflow → Create one**:

First, decide which node type to use based on the user's connections:

```bash
agenticflow connections list --json
```

| User has `pixelml` connection? | Node type to use | Connection needed? |
|-------------------------------|-----------------|-------------------|
| **Yes** | `generate_image` (provider: "Nano Banana 2") | Yes — set `"connection": "{{__app_connections__['<pixelml_connection_id>']}}"` |
| **No** | `agenticflow_generate_image` (Powered by AgenticFlow) | No — set `"connection": null` |

**Node type comparison**:

| | `generate_image` | `agenticflow_generate_image` |
|---|---|---|
| Connection | Requires `pixelml` | None required |
| Providers | Nano Banana 2, Runware, etc. | AgenticFlow built-in |
| Required fields | `prompt`, `negative_prompt`, `aspect_ratio` | `prompt`, `aspect_ratio` |
| Optional fields | `provider`, `model_id`, `lora` | `model`, `negative_prompt`, `format` |

**Create workflow — Option A: With PixelML connection** (higher quality, more providers):

```bash
cat > /tmp/af-slide-imagegen.json << 'WFEOF'
{
  "name": "Slide Deck Image Generator",
  "description": "Generates slide images from text prompts. Used by the slide-deck skill.",
  "input_schema": {
    "type": "object",
    "title": "User inputs",
    "required": ["prompt"],
    "properties": {
      "prompt": {
        "type": "string",
        "title": "Image Prompt",
        "description": "Detailed prompt for slide image generation",
        "ui_metadata": {
          "type": "long_text",
          "order": 0,
          "value": "",
          "placeholder": "Describe the slide image..."
        }
      }
    }
  },
  "nodes": {
    "nodes": [
      {
        "name": "generate_image",
        "title": "Generate Slide Image",
        "description": "Generate a slide image from prompt",
        "node_type_name": "generate_image",
        "input_config": {
          "prompt": "{{prompt}}",
          "provider": "Nano Banana 2",
          "aspect_ratio": "16:9 (1K)",
          "negative_prompt": "NSFW, blurry, low quality, watermark, text artifacts",
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

Replace `<PIXELML_CONNECTION_ID>` with the actual `id` from `agenticflow connections list` where `category == "pixelml"`.

**Create workflow — Option B: Without connection** (works for any user):

```bash
cat > /tmp/af-slide-imagegen.json << 'WFEOF'
{
  "name": "Slide Deck Image Generator",
  "description": "Generates slide images from text prompts. Used by the slide-deck skill.",
  "input_schema": {
    "type": "object",
    "title": "User inputs",
    "required": ["prompt"],
    "properties": {
      "prompt": {
        "type": "string",
        "title": "Image Prompt",
        "description": "Detailed prompt for slide image generation",
        "ui_metadata": {
          "type": "long_text",
          "order": 0,
          "value": "",
          "placeholder": "Describe the slide image..."
        }
      }
    }
  },
  "nodes": {
    "nodes": [
      {
        "name": "generate_image",
        "title": "Generate Slide Image",
        "description": "Generate a slide image from prompt (AgenticFlow built-in)",
        "node_type_name": "agenticflow_generate_image",
        "input_config": {
          "prompt": "{{prompt}}",
          "aspect_ratio": "16:9",
          "negative_prompt": "NSFW, blurry, low quality, watermark, text artifacts",
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

**Then create**:
```bash
agenticflow workflow create --body @/tmp/af-slide-imagegen.json --json
```

**Store the returned `id`** as the `workflow_id`. Optionally save it to EXTEND.md for future sessions:
```yaml
agenticflow:
  workflow_id: "<returned_workflow_id>"
```

**0.5 Test the workflow** (recommended on first use):

```bash
cat > /tmp/af-test-input.json << 'EOF'
{
  "prompt": "A professional slide cover with the title 'Test' in modern minimalist style, 16:9 aspect ratio"
}
EOF

agenticflow workflow run --workflow-id <workflow_id> --input @/tmp/af-test-input.json --json
```

Then poll status:
```bash
agenticflow workflow run-status --workflow-run-id <run_id> --json
```

If the test succeeds, the workflow is ready. Proceed to Step 1.

---

### Step 1: Setup & Analyze

**1.1 Load Preferences (EXTEND.md)**

Check EXTEND.md existence (priority order):

```bash
# macOS, Linux, WSL, Git Bash
test -f .agent-skills/slide-deck/EXTEND.md && echo "project"
test -f "${XDG_CONFIG_HOME:-$HOME/.config}/agent-skills/slide-deck/EXTEND.md" && echo "xdg"
test -f "$HOME/.agent-skills/slide-deck/EXTEND.md" && echo "user"
```

| Path | Location |
|------|----------|
| `.agent-skills/slide-deck/EXTEND.md` | Project directory |
| `$HOME/.agent-skills/slide-deck/EXTEND.md` | User home |

**When EXTEND.md Found** → Read, parse, **output summary to user**:

```
Loaded preferences from [full path]
- Style: [preset/custom name]
- Audience: [audience or "auto-detect"]
- Language: [language or "auto-detect"]
- Review: [enabled/disabled]
```

**When EXTEND.md Not Found** → First-time setup using AskUserQuestion or proceed with defaults.

**EXTEND.md Supports**: Preferred style | Custom dimensions | Default audience | Language preference | Review preference | AgenticFlow workflow ID (for image generation)

Schema: `references/config/preferences-schema.md`

**1.2 Analyze Content**

1. Save source content (if pasted, save as `source.md`)
   - **Backup rule**: If `source.md` exists, rename to `source-backup-YYYYMMDD-HHMMSS.md`
2. Follow `references/analysis-framework.md` for content analysis
3. Analyze content signals for style recommendations
4. Detect source language
5. Determine recommended slide count
6. Generate topic slug from content

**1.3 Check Existing Content**

**MUST execute before proceeding to Step 2.**

Use Bash to check if output directory exists:

```bash
test -d "slide-deck/{topic-slug}" && echo "exists"
```

**If directory exists**, use AskUserQuestion:

```
header: "Existing"
question: "Existing content found. How to proceed?"
options:
  - label: "Regenerate outline"
    description: "Keep images, regenerate outline only"
  - label: "Regenerate images"
    description: "Keep outline, regenerate images only"
  - label: "Backup and regenerate"
    description: "Backup to {slug}-backup-{timestamp}, then regenerate all"
  - label: "Exit"
    description: "Cancel, keep existing content unchanged"
```

**Save to `analysis.md`** with:
- Topic, audience, content signals
- Recommended style (based on Auto Style Selection)
- Recommended slide count
- Language detection

### Step 2: Confirmation

**Two-round confirmation**: Round 1 always, Round 2 only if "Custom dimensions" selected.

**Language**: Use user's input language or saved language preference.

**Display summary**:
- Content type + topic identified
- Language: [from EXTEND.md or detected]
- **Recommended style**: [preset] (based on content signals)
- **Recommended slides**: [N] (based on content length)

#### Round 1 (Always)

**Use AskUserQuestion** for all 5 questions:

**Question 1: Style**
```
header: "Style"
question: "Which visual style for this deck?"
options:
  - label: "{recommended_preset} (Recommended)"
    description: "Best match based on content analysis"
  - label: "{alternative_preset}"
    description: "[alternative style description]"
  - label: "Custom dimensions"
    description: "Choose texture, mood, typography, density separately"
```

**Question 2: Audience**
```
header: "Audience"
question: "Who is the primary reader?"
options:
  - label: "General readers (Recommended)"
    description: "Broad appeal, accessible content"
  - label: "Beginners/learners"
    description: "Educational focus, clear explanations"
  - label: "Experts/professionals"
    description: "Technical depth, domain knowledge"
  - label: "Executives"
    description: "High-level insights, minimal detail"
```

**Question 3: Slide Count**
```
header: "Slides"
question: "How many slides?"
options:
  - label: "{N} slides (Recommended)"
    description: "Based on content length"
  - label: "Fewer ({N-3} slides)"
    description: "More condensed, less detail"
  - label: "More ({N+3} slides)"
    description: "More detailed breakdown"
```

**Question 4: Review Outline**
```
header: "Outline"
question: "Review outline before generating prompts?"
options:
  - label: "Yes, review outline (Recommended)"
    description: "Review slide titles and structure"
  - label: "No, skip outline review"
    description: "Proceed directly to prompt generation"
```

**Question 5: Review Prompts**
```
header: "Prompts"
question: "Review prompts before generating images?"
options:
  - label: "Yes, review prompts (Recommended)"
    description: "Review image generation prompts"
  - label: "No, skip prompt review"
    description: "Proceed directly to image generation"
```

#### Round 2 (Only if "Custom dimensions" selected)

**Use AskUserQuestion** for all 4 dimensions:

**Question 1: Texture**
```
header: "Texture"
question: "Which visual texture?"
options:
  - label: "clean"
    description: "Pure solid color, no texture"
  - label: "grid"
    description: "Subtle grid overlay, technical"
  - label: "organic"
    description: "Soft textures, hand-drawn feel"
  - label: "pixel"
    description: "Chunky pixels, 8-bit aesthetic"
```
(Note: "paper" available via Other)

**Question 2: Mood**
```
header: "Mood"
question: "Which color mood?"
options:
  - label: "professional"
    description: "Cool-neutral, navy/gold"
  - label: "warm"
    description: "Earth tones, friendly"
  - label: "cool"
    description: "Blues, grays, analytical"
  - label: "vibrant"
    description: "High saturation, bold"
```
(Note: "dark", "neutral" available via Other)

**Question 3: Typography**
```
header: "Typography"
question: "Which typography style?"
options:
  - label: "geometric"
    description: "Modern sans-serif, clean"
  - label: "humanist"
    description: "Friendly, readable"
  - label: "handwritten"
    description: "Marker/brush, organic"
  - label: "editorial"
    description: "Magazine style, dramatic"
```
(Note: "technical" available via Other)

**Question 4: Density**
```
header: "Density"
question: "Information density?"
options:
  - label: "balanced (Recommended)"
    description: "2-3 key points per slide"
  - label: "minimal"
    description: "One focus point, maximum whitespace"
  - label: "dense"
    description: "Multiple data points, compact"
```

**After Round 2**: Store custom dimensions as the style configuration.

**After Confirmation**:
1. Update `analysis.md` with confirmed preferences
2. Store `skip_outline_review` flag from Question 4
3. Store `skip_prompt_review` flag from Question 5
4. → Step 3

### Step 3: Generate Outline

Create outline using the confirmed style from Step 2.

**Style Resolution**:
- If preset selected → Read `references/styles/{preset}.md`
- If custom dimensions → Read dimension files from `references/dimensions/` and combine

**Generate**:
1. Follow `references/outline-template.md` for structure
2. Build STYLE_INSTRUCTIONS from style or dimensions
3. Apply confirmed audience, language, slide count
4. Save as `outline.md`

**After generation**:
- If `--outline-only`, stop here
- If `skip_outline_review` is true → Skip Step 4, go to Step 5
- If `skip_outline_review` is false → Continue to Step 4

### Step 4: Review Outline (Conditional)

**Skip this step** if user selected "No, skip outline review" in Step 2.

**Purpose**: Review outline structure before prompt generation.

**Language**: Use user's input language or saved language preference.

**Display**:
- Total slides: N
- Style: [preset name or "custom: texture+mood+typography+density"]
- Slide-by-slide summary table:

```
| # | Title | Type | Layout |
|---|-------|------|--------|
| 1 | [title] | Cover | title-hero |
| 2 | [title] | Content | [layout] |
| 3 | [title] | Content | [layout] |
| ... | ... | ... | ... |
```

**Use AskUserQuestion**:
```
header: "Confirm"
question: "Ready to generate prompts?"
options:
  - label: "Yes, proceed (Recommended)"
    description: "Generate image prompts"
  - label: "Edit outline first"
    description: "I'll modify outline.md before continuing"
  - label: "Regenerate outline"
    description: "Create new outline with different approach"
```

**After response**:
1. If "Edit outline first" → Inform user to edit `outline.md`, ask again when ready
2. If "Regenerate outline" → Back to Step 3
3. If "Yes, proceed" → Continue to Step 5

### Step 5: Generate Prompts

1. Read `references/base-prompt.md`
2. For each slide in outline:
   - Extract STYLE_INSTRUCTIONS from outline (not from style file again)
   - Add slide-specific content
   - If `Layout:` specified, include layout guidance from `references/layouts.md`
3. Save to `prompts/` directory
   - **Backup rule**: If prompt file exists, rename to `prompts/NN-slide-{slug}-backup-YYYYMMDD-HHMMSS.md`

**After generation**:
- If `--prompts-only`, stop here and output prompt summary
- If `skip_prompt_review` is true → Skip Step 6, go to Step 7
- If `skip_prompt_review` is false → Continue to Step 6

### Step 6: Review Prompts (Conditional)

**Skip this step** if user selected "No, skip prompt review" in Step 2.

**Purpose**: Review prompts before image generation.

**Language**: Use user's input language or saved language preference.

**Display**:
- Total prompts: N
- Style: [preset name or custom dimensions]
- Prompt list:

```
| # | Filename | Slide Title |
|---|----------|-------------|
| 1 | 01-slide-cover.md | [title] |
| 2 | 02-slide-xxx.md | [title] |
| ... | ... | ... |
```

- Path to prompts directory: `prompts/`

**Use AskUserQuestion**:
```
header: "Confirm"
question: "Ready to generate slide images?"
options:
  - label: "Yes, proceed (Recommended)"
    description: "Generate all slide images"
  - label: "Edit prompts first"
    description: "I'll modify prompts before continuing"
  - label: "Regenerate prompts"
    description: "Create new prompts with different approach"
```

**After response**:
1. If "Edit prompts first" → Inform user to edit prompts, ask again when ready
2. If "Regenerate prompts" → Back to Step 5
3. If "Yes, proceed" → Continue to Step 7

### Step 7: Generate Images via AgenticFlow

**For `--images-only`**: Start here with existing prompts.

**For `--regenerate N`**: Only regenerate specified slide(s).

**Standard flow**:

1. **Use the AgenticFlow workflow** from Step 0 (stored `workflow_id`)
2. For each slide prompt file in `prompts/`:
   a. Read the prompt content from the `.md` file
   b. **Backup rule**: If image file exists, rename to `NN-slide-{slug}-backup-YYYYMMDD-HHMMSS.png`
   c. Create input JSON and run workflow:

   ```bash
   # Write prompt to temp file
   cat > /tmp/af-slide-input.json << 'EOF'
   {
     "prompt": "<full prompt text from the slide prompt file>"
   }
   EOF

   # Run the image generation workflow
   agenticflow workflow run --workflow-id <workflow_id> --input @/tmp/af-slide-input.json --json
   ```

   d. **Poll for completion**:
   ```bash
   agenticflow workflow run-status --workflow-run-id <run_id> --json
   ```
   Keep polling until `status` is `success` or `failed`. Wait 3-5 seconds between polls.

   e. **Extract image URL** from the run output:
   The `generate_image` node outputs `{ "image": "<url>", "content": ... }`.
   Access it from: `output.generate_image.image` or `state.nodes_state[0].output.image`

   f. **Download image** to local file:
   ```bash
   curl -sL "<image_url>" -o "slide-deck/{topic-slug}/NN-slide-{slug}.png"
   ```

3. Report progress: "Generated X/N" (in user's language)
4. Auto-retry once on failure before reporting error

**Error Handling**:
- If workflow run fails with connection error → prompt user to set up connection via AgenticFlow web UI
- If image generation fails → retry once, then report which slides failed
- If all retries fail → save partial results and inform user

### Step 8: Merge to PPTX and PDF

```bash
${BUN_X} {baseDir}/scripts/merge-to-pptx.ts <slide-deck-dir>
${BUN_X} {baseDir}/scripts/merge-to-pdf.ts <slide-deck-dir>
```

### Step 9: Output Summary

**Language**: Use user's input language or saved language preference.

```
Slide Deck Complete!

Topic: [topic]
Style: [preset name or custom dimensions]
Location: [directory path]
Slides: N total
Image Generation: AgenticFlow (workflow: <workflow_id>)

- 01-slide-cover.png - Cover
- 02-slide-intro.png - Content
- ...
- {NN}-slide-back-cover.png - Back Cover

Outline: outline.md
PPTX: {topic-slug}.pptx
PDF: {topic-slug}.pdf
```

## Partial Workflows

| Option | Workflow |
|--------|----------|
| `--outline-only` | Steps 1-3 only (stop after outline) |
| `--prompts-only` | Steps 1-5 (generate prompts, skip images) |
| `--images-only` | Skip to Step 7 (requires existing prompts/) |
| `--regenerate N` | Regenerate specific slide(s) only |

### Using `--prompts-only`

Generate outline and prompts without images:

```bash
/slide-deck content.md --prompts-only
```

Output: `outline.md` + `prompts/*.md` ready for review/editing.

### Using `--images-only`

Generate images from existing prompts (starts at Step 7):

```bash
/slide-deck slide-deck/topic-slug/ --images-only
```

Prerequisites:
- `prompts/` directory with slide prompt files
- `outline.md` with style information

### Using `--regenerate`

Regenerate specific slides:

```bash
# Single slide
/slide-deck slide-deck/topic-slug/ --regenerate 3

# Multiple slides
/slide-deck slide-deck/topic-slug/ --regenerate 2,5,8
```

Flow:
1. Read existing prompts for specified slides
2. Regenerate images only for those slides via AgenticFlow
3. Regenerate PPTX/PDF

## Slide Modification

### Quick Reference

| Action | Command | Manual Steps |
|--------|---------|--------------|
| **Edit** | `--regenerate N` | **Update prompt file FIRST** → Regenerate image → Regenerate PDF |
| **Add** | Manual | Create prompt → Generate image → Renumber subsequent → Update outline → Regenerate PDF |
| **Delete** | Manual | Remove files → Renumber subsequent → Update outline → Regenerate PDF |

### Edit Single Slide

1. **Update prompt file FIRST** in `prompts/NN-slide-{slug}.md`
2. Run: `/slide-deck <dir> --regenerate N`
3. Or manually regenerate image + PDF

**IMPORTANT**: When updating slides, ALWAYS update the prompt file (`prompts/NN-slide-{slug}.md`) FIRST before regenerating. This ensures changes are documented and reproducible.

### Add New Slide

1. Create prompt at position: `prompts/NN-slide-{new-slug}.md`
2. Generate image via AgenticFlow workflow
3. **Renumber**: Subsequent files NN+1 (slugs unchanged)
4. Update `outline.md`
5. Regenerate PPTX/PDF

### Delete Slide

1. Remove `NN-slide-{slug}.png` and `prompts/NN-slide-{slug}.md`
2. **Renumber**: Subsequent files NN-1 (slugs unchanged)
3. Update `outline.md`
4. Regenerate PPTX/PDF

### File Naming

Format: `NN-slide-[slug].png`
- `NN`: Two-digit sequence (01, 02, ...)
- `slug`: Kebab-case from content (2-5 words, unique)

**Renumbering Rule**: Only NN changes, slugs remain unchanged.

See `references/modification-guide.md` for complete details.

## References

| File | Content |
|------|---------|
| `references/analysis-framework.md` | Content analysis for presentations |
| `references/outline-template.md` | Outline structure and format |
| `references/modification-guide.md` | Edit, add, delete slide workflows |
| `references/content-rules.md` | Content and style guidelines |
| `references/design-guidelines.md` | Audience, typography, colors, visual elements |
| `references/layouts.md` | Layout options and selection tips |
| `references/base-prompt.md` | Base prompt for image generation |
| `references/dimensions/*.md` | Dimension specifications (texture, mood, typography, density) |
| `references/dimensions/presets.md` | Preset → dimension mapping |
| `references/styles/<style>.md` | Full style specifications (legacy) |
| `references/config/preferences-schema.md` | EXTEND.md structure |

## Notes

- Image generation via AgenticFlow: 10-30 seconds per slide
- Auto-retry once on generation failure
- Use stylized alternatives for sensitive public figures
- **Step 2 confirmation required** - do not skip (style, audience, slides, outline review, prompt review)
- **Step 4 conditional** - only if user requested outline review in Step 2
- **Step 6 conditional** - only if user requested prompt review in Step 2
- AgenticFlow workflow must be set up before first image generation (Step 0)

## Extension Support

Custom configurations via EXTEND.md. See **Step 1.1** for paths and supported options.

Additional EXTEND.md field for AgenticFlow:
```yaml
agenticflow:
  workflow_id: "<your-image-gen-workflow-id>"
  provider: "Nano Banana 2"
  aspect_ratio: "16:9 (1K)"
```
