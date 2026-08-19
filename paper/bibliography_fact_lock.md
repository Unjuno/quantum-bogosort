# Bibliography Fact Lock

This table locks the **reviewed current-main bibliography facts** used by the pre-announcement prior-art audit. It is a regression contract, not an automated claim that external bibliographic truth can be proved from repository-local data.

The policy is:

- `definitive-publication` — a verified journal article or book chapter is used as the canonical manuscript record;
- `retained-early-preprint` — an earlier public preprint is intentionally retained because it is the relevant early prior-art record and is not silently collapsed into a later revised bibliographic identity;
- `retained-preprint` — no definitive same-work publication was established in the audit pass;
- `retained-working-paper` — the current source is still presented by its authors as a working paper/preprint;
- `latest-working-preprint` — author archival provenance identifies the cited preprint as the latest version of the same-title working paper.

The validator checks that `paper/references.bib` has exactly the same citation-key set, record class, year, and canonical DOI/arXiv identifier. External factual re-verification remains a human review task.

| citation_key | record_type | year | canonical_id | provenance |
|---|---|---:|---|---|
| wallace2009born | misc | 2009 | arxiv:0906.2718 | retained-early-preprint |
| greaves2004deutsch | article | 2004 | doi:10.1016/j.shpsb.2004.04.006 | definitive-publication |
| sebenscarroll2018selflocating | article | 2018 | doi:10.1093/bjps/axw004 | definitive-publication |
| lewis2009selflocation | article | 2009 | doi:10.1086/605805 | definitive-publication |
| saunders2010chance | incollection | 2010 | doi:10.1093/acprof:oso/9780199560561.003.0008 | definitive-publication |
| saunders2021probability | incollection | 2021 | doi:10.4324/9781315623818-21 | definitive-publication |
| saunders2021branchcounting | article | 2021 | doi:10.1098/rspa.2021.0600 | definitive-publication |
| saunders2026physicalprobability | misc | 2026 | arxiv:2601.12159 | latest-working-preprint |
| khawaja2026branchcounting | article | 2026 | doi:10.1086/726282 | definitive-publication |
| tegmark1997manywords | misc | 1997 | arxiv:quant-ph/9709032 | retained-early-preprint |
| mallah2009immortality | misc | 2009 | arxiv:0902.0187 | retained-preprint |
| hanson2003mangled | article | 2003 | doi:10.1023/A:1025642019178 | definitive-publication |
| garisto2020selectobservers | article | 2020 | doi:10.1103/PhysRevResearch.2.033464 | definitive-publication |
| armstrong2011anthropic | misc | 2011 | arxiv:1110.6437 | retained-preprint |
| price2006probability | misc | 2006 | arxiv:quant-ph/0604191 | retained-preprint |
| price2010decisions | incollection | 2010 | doi:10.1093/acprof:oso/9780199560561.003.0014 | definitive-publication |
| kent2010oneworld | incollection | 2010 | doi:10.1093/acprof:oso/9780199560561.003.0012 | definitive-publication |
| araujo2019deterministic | article | 2019 | doi:10.1007/s10701-019-00241-7 | definitive-publication |
| hultnyquist2016importance | article | 2016 | doi:10.1016/j.spa.2015.08.002 | definitive-publication |
| conitzer2015dese | article | 2015 | doi:10.1007/s11229-015-0737-x | definitive-publication |
| cooperoesterheldconitzer2024anthropics | misc | 2024 | arxiv:2411.04462 | retained-working-paper |

See [`../docs/pre_announcement_bibliography_audit_2026-08-19.md`](../docs/pre_announcement_bibliography_audit_2026-08-19.md) for the external-review rationale and chronology policy.