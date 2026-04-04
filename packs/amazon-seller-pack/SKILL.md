# Amazon Seller Pack

AI skills for Amazon Singapore sellers. Part of the AgenticFlow Starter Pack for Amazon Selling Partners.

## Skills

### Atomic Skills
- **listing-optimizer** — Optimize product title, bullets, description, backend keywords for A9/A10 algorithm
- **keyword-researcher** — Research high-value keywords including multilingual terms (English, Mandarin, Malay)
- **review-analyzer** — Extract insights from customer reviews — sentiment, complaints, competitive intelligence
- **ppc-campaign-planner** — Plan Sponsored Products/Brands/Display campaigns with bid strategy and budget allocation
- **competitor-monitor** — Analyze competitor pricing, listings, reviews, and market positioning
- **pricing-strategist** — Develop pricing strategy with FBA fee calculations and SG promotional calendar
- **customer-response** — Draft Amazon-compliant customer responses for messages, reviews, and Q&A

### Composed Skills
- **product-launcher** — Full launch pipeline: keywords → listing → pricing → PPC campaign

### Workflows
- **product-launch** — Single-step comprehensive launch plan covering all aspects

## Deploy as a Paperclip Company

```bash
af paperclip init --blueprint amazon-seller
af gateway serve --channels paperclip
af paperclip connect
```

This creates a 5-agent Amazon seller team:
- Amazon Business Manager (CEO) — strategy and coordination
- Listing & SEO Specialist (CMO) — listing optimization
- PPC Campaign Manager (Engineer) — advertising
- Market & Competitor Analyst (Researcher) — intelligence
- Customer Support Agent (General) — buyer communication

## Target Market
Amazon Singapore Selling Partners using AgenticFlow via the AWS partner program.
