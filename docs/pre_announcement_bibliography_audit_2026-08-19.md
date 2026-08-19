# Pre-announcement bibliography and prior-art truth audit — 2026-08-19

## Purpose

This pass asks a question that syntax-only bibliography validation cannot answer: **do the manuscript and prior-art ledgers identify the correct public/definitive records and chronology for the works they rely on?**

A BibTeX record can be syntactically valid while still making established prior art appear artificially recent by citing a later arXiv upload instead of an earlier journal or book publication. Because QBS makes a deliberately narrow and provisional novelty claim, publication chronology is part of the scientific audit rather than a cosmetic bibliography issue.

This pass therefore cross-checked the current bibliography and literature ledgers against publisher, journal, author-publication, and archival records where available.

## Provenance policy used

The audit uses the following rule rather than mechanically replacing every preprint:

1. use a verified journal or book publication when it is clearly the definitive publication of the same work and a later preprint posting would obscure publication chronology;
2. retain an earlier public preprint when it is itself the relevant early prior-art record, even if a later publication exists under revised bibliographic form or title;
3. retain a preprint/working-paper record when no definitive publication record was identified;
4. do not silently equate records whose title or publication identity materially changed;
5. distinguish bibliography syntax validation from external factual verification.

## Verified publication corrections

### Greaves

`Understanding Deutsch's probability in a deterministic multiverse` is represented by the 2004 journal publication in *Studies in History and Philosophy of Science Part B*, 35(3), 423–456, DOI `10.1016/j.shpsb.2004.04.006`, rather than only the 2003 arXiv posting.

### Sebens and Carroll

`Self-Locating Uncertainty and the Origin of Probability in Everettian Quantum Mechanics` is represented by the 2018 *British Journal for the Philosophy of Science* publication, 69(1), 25–74, DOI `10.1093/bjps/axw004`, rather than only the 2014 preprint.

### Saunders — chance

`Chance in the Everett Interpretation` is represented as the 2010 Oxford University Press chapter in *Many Worlds? Everett, Quantum Theory, and Reality*, pp. 181–205, DOI `10.1093/acprof:oso/9780199560561.003.0008`.

The audit encountered a conflicting secondary page-range citation. Oxford primary metadata confirms pp. 181–205, which is the range retained and fact-locked in the repository. The conflicting 355–368 range belongs to a different chapter in the same volume and is not used for this record.

### Saunders — Everett probability

`The Everett Interpretation: Probability` is represented as a 2021 chapter in *The Routledge Companion to Philosophy of Physics*, pp. 230–246, DOI `10.4324/9781315623818-21`, rather than as an arXiv-only record.

### Saunders — branch counting

`Branch-counting in the Everett Interpretation of quantum mechanics` is represented by the 2021 *Proceedings of the Royal Society A* article, 477(2255), 20210600, DOI `10.1098/rspa.2021.0600`.

### Hanson

`When Worlds Collide: Quantum Probability From Observer Selection?` is represented by its 2003 *Foundations of Physics* publication, 33(7), 1129–1150, DOI `10.1023/A:1025642019178`, rather than only the 2001 preprint.

### Garisto

`How to Select Observers` is represented by the 2020 *Physical Review Research* article, 2(3), 033464, DOI `10.1103/PhysRevResearch.2.033464`.

### Price — decisions

`Decisions, Decisions, Decisions: Can Savage Salvage Everettian Probability?` is represented by the 2010 Oxford University Press chapter in *Many Worlds? Everett, Quantum Theory, and Reality*, pp. 369–390, DOI `10.1093/acprof:oso/9780199560561.003.0014`.

### Kent

`One World Versus Many: The Inadequacy of Everettian Accounts of Evolution, Probability, and Scientific Confirmation` is represented by the 2010 Oxford University Press chapter in *Many Worlds? Everett, Quantum Theory, and Reality*, pp. 307–354, DOI `10.1093/acprof:oso/9780199560561.003.0012`.

### Araújo

`Probability in Two Deterministic Universes` is represented by the 2019 *Foundations of Physics* article, 49(3), 202–231, DOI `10.1007/s10701-019-00241-7`, rather than only the 2018 preprint.

### Hult and Nyquist

`Large deviations for weighted empirical measures arising in importance sampling` is represented by the 2016 *Stochastic Processes and their Applications* article, 126(1), 138–170, DOI `10.1016/j.spa.2015.08.002`, rather than only the 2012 preprint.

### Conitzer

`Can rational choice guide us to correct de se beliefs?` is represented by the 2015 *Synthese* publication, 192(12), 4107–4119, DOI `10.1007/s11229-015-0737-x`.

This correction is chronology-relevant: the repository previously used a later 2017 arXiv posting, which could make the prior work appear newer than it is.

### Khawaja

The current *British Journal for the Philosophy of Science* entry for `Conquering Mount Everett: Branch Counting Versus the Born Rule` now includes the verified page range 313–344 in volume 77(2), DOI `10.1086/726282`.

## Preprint records intentionally retained

### Wallace

`A formal proof of the Born rule from decision-theoretic assumptions`, arXiv:0906.2718 (2009), is retained as the earlier public record. A later Oxford chapter appears in revised-title form as `How to Prove the Born Rule`; the audit does not silently collapse the two records into one bibliographic identity.

### Tegmark

The 1997 arXiv record for `The Interpretation of Quantum Mechanics: Many Worlds or Many Words?` is retained because it is the earlier public prior-art record. The literature ledger also notes the 1998 *Fortschritte der Physik* publication.

### Mallah

`Many-Worlds Interpretations Can Not Imply 'Quantum Immortality'`, arXiv:0902.0187, remains a preprint record because no definitive same-work publication was established in this pass.

### Armstrong

`Anthropic decision theory`, arXiv:1110.6437, remains a preprint record because no definitive same-work publication was established in this pass.

### Price — 2006 comments

`Probability in the Everett World: Comments on Wallace and Greaves`, arXiv:quant-ph/0604191, remains a preprint record; no definitive same-title publication was established in this pass.

### Cooper, Oesterheld, and Conitzer

`Can CDT rationalise the ex ante optimal policy via modified anthropics?`, arXiv:2411.04462, remains a working-paper/preprint record. The authors' current publication listing still classifies it as a working paper.

### Saunders — physical probability and Bell inequalities

The current bibliography retains arXiv:2601.12159. Author archival provenance identifies the 2026 deposit as the latest version and links the same-title 2025 deposit as an earlier available version.

## Bibliography validator correction

The previous bibliography validator could verify syntax and DOI/arXiv formatting but could not enforce complete publication-container metadata. It now distinguishes three provenance classes:

- journal `@article`: requires `journal`, `volume`, `pages`, and DOI;
- book-chapter `@incollection`: requires `booktitle`, `editor`, `publisher`, `pages`, and DOI;
- arXiv-only `@misc`: requires eprint/archive/class metadata and excludes publication-container fields.

The repository uses stock `plain.bst`, so DOI-bearing records also retain a printable `note = {doi:...}` field.

A second false-PASS remained after that correction: once publication chronology had been externally reviewed, a later edit could still silently change the citation key, record class, year, or canonical identifier while remaining syntactically valid. A first version of [`../paper/bibliography_fact_lock.md`](../paper/bibliography_fact_lock.md) closed that gap.

A third false-PASS then became visible: the initial fact lock did **not** lock author strings, titles, journal/book container metadata, volume/number, or pages/article numbers. A record could therefore keep the same DOI/year while acquiring a wrong title, author, or page range and still pass. That is material because this audit itself encountered a real conflicting secondary page-range citation for the Saunders chance chapter.

The reviewed fact lock now records, for every current bibliography entry:

- citation key;
- BibTeX record type;
- publication/preprint year;
- author string;
- title string;
- publication locator;
- canonical DOI or arXiv identifier;
- provenance class.

For journal articles, the locator fixes journal, volume/number, and pages/article number. For book chapters, it fixes book title, editors, publisher, and pages. For retained preprints, the locator is explicitly `arXiv`. `scripts/validate_bibliography_metadata.py` requires exact agreement between all of those reviewed values and `references.bib`.

The fact lock is a regression guard, not an oracle. It prevents accidental reversal or corruption of already-reviewed bibliography facts; external factual truth still cannot be proved by a repository-local parser and remains a review responsibility.

## Prior-art semantic drift found

All three working literature ledgers contained older wording that described recognition as a `causal variable` or `causal policy input`.

That wording was inconsistent with the current authoritative QBS boundary. The ledgers now state the intended relationship:

- recognition/information state may change which policy is selected;
- the selected policy may causally change trajectories and may change accessibility;
- recognition itself is not assigned privileged physical causal power merely by appearing upstream in the model.

The authoritative theorem/claim sources did not require this correction; the drift was localized to the literature-review layer.

## Current novelty boundary after this pass

The bibliography corrections **narrow and stabilize** the novelty framing rather than strengthening it artificially. The repository continues not to claim novelty for:

- Everettian decision theory;
- caring measures;
- self-locating uncertainty;
- observer selection;
- anthropic/copy decision theory;
- self-location changing action recommendations;
- normalized weighting or change of measure;
- covariance and total-covariance identities;
- branch-sensitive physical-probability proposals.

The provisional contribution remains the combined recognition/information-state → policy → trajectory/accessibility architecture, exact trajectory/conditioning and interaction decompositions, predictive-alignment/general-accessibility stack, and separation of marginal first-person uplift from cross-copy coherence.

Failure to find a direct structural duplicate remains **not evidence of absence**.

## Source-diff boundary

Relative to the start of this bibliography truth pass, the changed surface is limited to:

- `paper/references.bib`;
- `paper/sections/related_work.tex`;
- `paper/bibliography_fact_lock.md` and `paper/README.md`;
- the three `literature/` prior-art ledgers;
- `scripts/validate_bibliography_metadata.py` and the repository-structure inventory needed to require the fact lock;
- changelog/status/audit documentation.

The pass does not modify:

- `theory/` theorem sources;
- S2-family supplementary theorem/certificate sources;
- E1–E5 experiment scripts or results;
- committed data outputs;
- figure generators or committed SVG figures;
- the Everett bridge status.

## Remaining gate

The bibliography/Related Work edits and reviewed fact-lock validator must still pass the final manuscript/repository GitHub Actions jobs. Source-level citation-key alignment has been reviewed, but the final Actions execution result remains the authoritative build/CI gate.
