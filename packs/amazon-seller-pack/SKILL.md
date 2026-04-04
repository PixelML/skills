# Amazon Seller Pack v3

Complete AI team for Amazon Singapore sellers. Powered by Gemma 4 31B on AgenticFlow, deployed to Paperclip.

## Quick Deploy

```bash
af paperclip init --blueprint amazon-seller
af gateway serve --channels paperclip &
af paperclip connect
```

This creates a 5-agent team on Paperclip with Gemma 4, 5 starter tasks, and a company goal.

## What's Inside

### 5 Agents (company.yaml)
| Agent | Role | What it does |
|---|---|---|
| Listing & SEO Specialist | CMO | Title, bullets, backend keywords (EN/ZH/MS), A+ content |
| PPC Campaign Manager | Engineer | SP/SB/SD campaigns, keyword bids, budget allocation |
| Competitor Analyst | Researcher | Pricing comparison, listing quality, market gaps |
| Customer Support | General | Amazon ToS compliant review responses |
| Pricing Strategist | CEO | FBA fee calc, margins, SG promotional calendar |

### 8 Skills
- **listing-optimizer** — A9/A10 optimized listings with multilingual keywords
- **keyword-researcher** — EN/ZH/MS keywords for Singapore market
- **review-analyzer** — Sentiment, complaints, competitive intelligence
- **ppc-campaign-planner** — Campaign structure with SGD bids
- **competitor-monitor** — Comparison tables with pricing gaps
- **pricing-strategist** — FBA fees, margins, SG event calendar
- **customer-response** — Amazon-compliant buyer message drafts
- **product-launcher** (composed) — Full launch pipeline

### 4 Workflows (with real data)
- **product-launch** — Comprehensive launch plan (LLM)
- **competitor-scrape** — Scrape 3 competitor URLs → AI analysis (web_scraping + LLM)
- **listing-audit** — Scrape your listing → audit + optimized copy (web_scraping + LLM)
- **review-scrape-respond** — Scrape reviews → sentiment + draft responses (web_scraping + LLM)

## Model
`agenticflow/gemma-4-31b-it` — Google Gemma 4 31B Dense, 256K context, Apache 2.0

## Tested With
BlendGo Pro 600ml Portable Blender (SGD 39.90, Amazon SG)
- 5 agents produced 17K+ chars of actionable output
- Listing: multilingual keywords, A+ modules, competitor positioning
- PPC: 3-campaign structure, SGD bids, negative keywords, break-even ACoS
- Competitor: comparison matrix, pricing gaps, exploitation strategy
- Support: 5 ToS-compliant templates with internal notes
- Pricing: FBA cost breakdown, event calendar, promotional tiers
