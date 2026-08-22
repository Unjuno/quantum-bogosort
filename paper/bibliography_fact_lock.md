# Bibliography Fact Lock

This table locks the **reviewed current-main bibliography facts** used by the pre-announcement prior-art audit. It is a regression contract, not an automated claim that external bibliographic truth can be proved from repository-local data.

The policy is:

- `definitive-publication` — a verified journal article or book chapter is used as the canonical manuscript record;
- `retained-early-preprint` — an earlier public preprint is intentionally retained because it is the relevant early prior-art record and is not silently collapsed into a later revised bibliographic identity;
- `retained-preprint` — no definitive same-work publication was established in the audit pass;
- `retained-working-paper` — the current source is still presented by its authors as a working paper/preprint;
- `latest-working-preprint` — author archival provenance identifies the cited preprint as the latest version of the same-title working paper.

The validator checks that `paper/references.bib` has exactly the same citation-key set, record class, year, author string, title string, publication locator, and canonical DOI/arXiv identifier. For a journal article, the locator locks journal, volume/number, and pages/article number. For a book chapter, it locks book title, editors, publisher, and pages. External factual re-verification remains a human review task.

| citation_key | record_type | year | author | title | locator | canonical_id | provenance |
|---|---|---:|---|---|---|---|---|
| wallace2009born | misc | 2009 | David Wallace | A formal proof of the {Born} rule from decision-theoretic assumptions | arXiv | arxiv:0906.2718 | retained-early-preprint |
| greaves2004deutsch | article | 2004 | Hilary Greaves | Understanding {Deutsch}'s probability in a deterministic multiverse | Studies in History and Philosophy of Science Part B: Studies in History and Philosophy of Modern Physics; 35(3); 423--456 | doi:10.1016/j.shpsb.2004.04.006 | definitive-publication |
| sebenscarroll2018selflocating | article | 2018 | Charles T. Sebens and Sean M. Carroll | Self-Locating Uncertainty and the Origin of Probability in {Everettian} Quantum Mechanics | The British Journal for the Philosophy of Science; 69(1); 25--74 | doi:10.1093/bjps/axw004 | definitive-publication |
| lewis2009selflocation | article | 2009 | Peter J. Lewis | Probability, Self-Location, and Quantum Branching | Philosophy of Science; 76(5); 1009--1019 | doi:10.1086/605805 | definitive-publication |
| saunders2010chance | incollection | 2010 | Simon Saunders | Chance in the {Everett} Interpretation | Many Worlds? Everett, Quantum Theory, and Reality; Simon Saunders and Jonathan Barrett and Adrian Kent and David Wallace; Oxford University Press; 181--205 | doi:10.1093/acprof:oso/9780199560561.003.0008 | definitive-publication |
| saunders2021probability | incollection | 2021 | Simon Saunders | The {Everett} Interpretation: Probability | The Routledge Companion to Philosophy of Physics; Eleanor Knox and Alastair Wilson; Routledge; 230--246 | doi:10.4324/9781315623818-21 | definitive-publication |
| saunders2021branchcounting | article | 2021 | Simon Saunders | Branch-counting in the {Everett} Interpretation of quantum mechanics | Proceedings of the Royal Society A: Mathematical, Physical and Engineering Sciences; 477(2255); 20210600 | doi:10.1098/rspa.2021.0600 | definitive-publication |
| saunders2026physicalprobability | misc | 2026 | Simon Saunders | Physical probability in the {Everett} interpretation and {Bell} inequalities | arXiv | arxiv:2601.12159 | latest-working-preprint |
| khawaja2026branchcounting | article | 2026 | Jake Khawaja | Conquering Mount {Everett}: Branch Counting Versus the {Born} Rule | The British Journal for the Philosophy of Science; 77(2); 313--344 | doi:10.1086/726282 | definitive-publication |
| tegmark1997manywords | misc | 1997 | Max Tegmark | The Interpretation of Quantum Mechanics: {Many Worlds} or {Many Words}? | arXiv | arxiv:quant-ph/9709032 | retained-early-preprint |
| mallah2009immortality | misc | 2009 | Jacques Mallah | Many-Worlds Interpretations Can Not Imply '{Quantum Immortality}' | arXiv | arxiv:0902.0187 | retained-preprint |
| hanson2003mangled | article | 2003 | Robin D. Hanson | When Worlds Collide: Quantum Probability From Observer Selection? | Foundations of Physics; 33(7); 1129--1150 | doi:10.1023/A:1025642019178 | definitive-publication |
| garisto2020selectobservers | article | 2020 | Robert Garisto | How to Select Observers | Physical Review Research; 2(3); 033464 | doi:10.1103/PhysRevResearch.2.033464 | definitive-publication |
| armstrong2011anthropic | misc | 2011 | Stuart Armstrong | Anthropic decision theory | arXiv | arxiv:1110.6437 | retained-preprint |
| price2006probability | misc | 2006 | Huw Price | Probability in the {Everett} World: Comments on {Wallace} and {Greaves} | arXiv | arxiv:quant-ph/0604191 | retained-preprint |
| price2010decisions | incollection | 2010 | Huw Price | Decisions, Decisions, Decisions: Can {Savage} Salvage {Everettian} Probability? | Many Worlds? Everett, Quantum Theory, and Reality; Simon Saunders and Jonathan Barrett and Adrian Kent and David Wallace; Oxford University Press; 369--390 | doi:10.1093/acprof:oso/9780199560561.003.0014 | definitive-publication |
| kent2010oneworld | incollection | 2010 | Adrian Kent | One world versus many: the inadequacy of {Everettian} accounts of evolution, probability, and scientific confirmation | Many Worlds? Everett, Quantum Theory, and Reality; Simon Saunders and Jonathan Barrett and Adrian Kent and David Wallace; Oxford University Press; 307--354 | doi:10.1093/acprof:oso/9780199560561.003.0012 | definitive-publication |
| araujo2019deterministic | article | 2019 | Mateus Araújo | Probability in two deterministic universes | Foundations of Physics; 49(3); 202--231 | doi:10.1007/s10701-019-00241-7 | definitive-publication |
| hultnyquist2016importance | article | 2016 | Henrik Hult and Pierre Nyquist | Large deviations for weighted empirical measures arising in importance sampling | Stochastic Processes and their Applications; 126(1); 138--170 | doi:10.1016/j.spa.2015.08.002 | definitive-publication |
| fisher1934ascertainment | article | 1934 | R. A. Fisher | The effect of methods of ascertainment upon the estimation of frequencies | Annals of Eugenics; 6(1); 13--25 | doi:10.1111/j.1469-1809.1934.tb02105.x | definitive-publication |
| patilrao1978weighted | article | 1978 | G. P. Patil and C. R. Rao | Weighted Distributions and Size-Biased Sampling with Applications to Wildlife Populations and Human Families | Biometrics; 34(2); 179--189 | doi:10.2307/2530008 | definitive-publication |
| conitzer2015dese | article | 2015 | Vincent Conitzer | Can rational choice guide us to correct de se beliefs? | Synthese; 192(12); 4107--4119 | doi:10.1007/s11229-015-0737-x | definitive-publication |
| cooperoesterheldconitzer2024anthropics | misc | 2024 | Emery Cooper and Caspar Oesterheld and Vincent Conitzer | Can {CDT} rationalise the ex ante optimal policy via modified anthropics? | arXiv | arxiv:2411.04462 | retained-working-paper |

The Fisher and Patil--Rao entries were added in the selection-equivalence audit after direct external verification of journal, volume/issue, page range, and DOI. Rao's 1965 ascertainment paper is retained in the repository literature ledger but not added to this manuscript fact lock because the current bibliography validator requires a DOI-backed canonical record for journal articles.

See [`../docs/pre_announcement_bibliography_audit_2026-08-19.md`](../docs/pre_announcement_bibliography_audit_2026-08-19.md) for the original external-review rationale and chronology policy; subsequent fact-lock additions must retain the same verification discipline.
