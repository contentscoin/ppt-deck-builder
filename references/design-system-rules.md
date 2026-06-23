# PPT Design System Rules

## Slide Roles

Use one primary role per slide:

- `cover`
- `agenda`
- `section_divider`
- `claim`
- `metric_kpi`
- `chart_table_data`
- `image_hero`
- `quote`
- `problem_solution`
- `product_demo`
- `process_timeline`
- `comparison_matrix`
- `team_people`
- `financial_ask`
- `appendix`

Split the slide if it combines multiple roles such as problem, product demo, chart, quote, and CTA.

## Title Rule

Prefer claim titles over topic labels.

- Weak: `Market Size`
- Strong: `The category is expanding faster than legacy tools can serve`

Title limits:

- Preferred: 5-8 words or 34-55 characters
- Hard limit: 70 characters or 10 words
- If longer, move conditions/context into subtitle, body, or notes

## Hierarchy Rule

Use at most three hierarchy levels:

1. main message: title, big number, section label
2. evidence: chart, image, table, diagram
3. support: caption, source, footer, note

If a fourth level is needed, split the slide.

## Rhythm Rule

- Add a rhythm shift every 5-8 slides: `section_divider`, `image_hero`, `quote`, or `big_number`.
- Avoid more than three consecutive dense data slides.
- Keep repeated report/guideline slides consistent with fixed title, footer, source, and margin positions.

## Typography Baseline

For 16:9 widescreen, 13.333 x 7.5 inch:

| Role | Recommended size |
| --- | ---: |
| Cover title | 54-72 pt |
| Editorial cover title | 72-96 pt |
| Section title | 44-64 pt |
| Slide title | 30-40 pt |
| Dense report title | 24-32 pt |
| Subtitle/kicker | 16-22 pt |
| Body | 16-20 pt |
| Dense body | 13-16 pt |
| Quote | 28-44 pt |
| Big number | 56-96 pt |
| Chart label | 10-13 pt |
| Table body | 10-12 pt |
| Caption/source | 7-10 pt |
| Footer/page number | 7-9 pt |

QA flags:

- body below 10 pt: high risk
- chart label below 9 pt: high risk
- caption/source below 7 pt: high risk

## Layout Baseline

| Element | Recommended value |
| --- | ---: |
| Default safe margin | 0.45-0.7 in |
| Premium/editorial margin | 0.8-1.1 in |
| Dense report margin | 0.35-0.5 in |
| Minimum text edge clearance | 0.4 in |
| Hero image band | 13.333 x 4.5-5.8 in |
| Split image panel | 6.3-6.8 x 7.5 in |
| Large visual panel | 7.0-9.0 x 4.5-5.8 in |
| 16:9 thumbnail/card | 3.2-4.6 x 1.8-2.6 in |
| Chart area | 7.5-11.5 x 3.8-5.5 in |
| Footer band | 0.22-0.35 in |

## Visual Mapping

| Source material | Slide role | Layout pattern |
| --- | --- | --- |
| Long core argument | `claim` | editorial text, data plus insight |
| Multiple summary points | `claim` or `agenda` | 3 cards, numbered findings |
| KPI/metric | `metric_kpi` | big number, KPI card |
| Table/numbers | `chart_table_data` | native chart, simplified table |
| Product screen | `product_demo` | annotated screenshot, 60%+ screen area |
| Interview/review | `quote` | large quote, portrait/context image |
| Process | `process_timeline` | 3-5 step timeline |
| Competitor/options | `comparison_matrix` | matrix, 2x2, feature table |
| Brand rule | `brand_guideline` | rule + example + application |
| Meeting decision | `financial_ask` or `appendix` | decision log, action matrix |
