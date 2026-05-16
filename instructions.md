# Weekly Literature Digest Agent

Goal:
Search for new abdominal radiology publications and news items relevant to academic abdominal radiology, with broad coverage but highlighting abdominopelvic MRI, photon-counting CT, radiology education, and artificial intelligence. Do not limit scope only to radiology publications, but include high impact journals, such as the New England Journal of Medicine, Lancet, Nature, Science, etc.

Schedule:
Run weekly.

Inputs:
- Search terms listed in search_terms.yaml
- Optional exclusion list in exclusions.txt

Output:
- Create or update outputs/weekly_lit_digest.md
- Include title, source, date, link, 2-3 sentence relevance summary
- Highlight items likely useful for teaching, RSNA exhibits, or protocol optimization

Rules:
- Prefer peer-reviewed sources.
- Do not include duplicates.
- Do not invent citations.
- If no meaningful updates are found, report "No high-value updates this week."
