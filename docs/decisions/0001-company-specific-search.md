# ADR 0001: Company-specific search approach

## Context
Job Radar currently opens predefined saved searches on LinkedIn and jobs.ch.
A natural extension is searching by specific target company rather than
generic keyword searches.

## Options considered
- **Direct scraping of career pages.** Ruled out: 22 target companies means
  22 different page structures, several JS-rendered, high maintenance cost
  for the value added.
- **Jooble API.** Swiss coverage for target companies was close to empty
  (0-1 results per company tested).
- **Adzuna API.** Returns real, current postings, but has no company-level
  query parameter. Requires client-side filtering against job descriptions
  plus a maintained company-alias list to separate genuine matches from noise.

## Decision
Build on Adzuna: broad keyword search, filtered client-side. A prototype
filter has been validated and returns usable results. Full pipeline
(config schema, rate-limit caching, alias/denylist maintenance) in progress.