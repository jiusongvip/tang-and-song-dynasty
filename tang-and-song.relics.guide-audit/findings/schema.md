# Schema / Structured Data Findings

## Homepage Schemas
Status: PASS (5 schema types detected)

1. Article -- headline, description, datePublished, dateModified, author, publisher
2. FAQPage -- 13 Q&A pairs (correctly structured)
3. Table -- about field only (minimal)
4. ItemList -- 18 TouristAttraction entries
5. BreadcrumbList -- single entry (homepage)

All valid JSON-LD.

## Detail Page Schemas
Status: FAIL -- CRITICAL

All 18 detail pages have broken JSON-LD due to {{}} escaping bug.
Affected:
- TouristAttraction schema per page (invalid)
- BreadcrumbList schema per page (invalid)

Neither schema type renders as rich results.

## Missing Schemas

1. Organization -- no org-level schema on any page
2. WebSite -- no site-level schema with SearchAction
3. ImageObject -- TouristAttraction entries lack image properties

## Validation Status
Homepage: Should pass Google Rich Results Test (Article, FAQPage)
Detail pages: Will FAIL Google Rich Results Test until {{}} bug is fixed
