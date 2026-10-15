# Attribution review

Four controls plus the AS#04 material delta; Yule counts are reported through Decorte, and corpus, script, formula and signary models remain authority-specific.

Existing source consultation receipts and limits are inherited exactly from the referenced native packets. This pass inspects those packets, not the underlying publications afresh. No exhaustive literature search, new autopsy or independent review is claimed.

The complete selections below name the finite native collections reviewed. Other repository records and the broader literature are outside this checkpoint. Case counts are review tasks, not inscriptions, independent witnesses or fully attributed alternative pairs.

| Complete native selection | Rows |
|---|---:|
| `research/disagreement-register.json/items` | 4 |

Use the case query to read the finding together with the complete native evidence, including any named author/publication, source locator, inspection state, qualification and source dependence. Missing metadata stays missing; a source ID alone is not proof of direct consultation.

```sh
python scripts/attribution_review.py --check
python scripts/attribution_review.py --case 'ARC-DIS-001'
python scripts/evidence_query.py --list attribution-review
```

| Review ID | Type | Finding | Remaining work |
|---|---|---|---|
| ARC-DIS-001 | COUNT_OR_IDENTITY | Yule’s claimed15/listed14 is reported through Decorte, whose own defined register has16. These are authority-specific corpus definitions, not competing observed object totals. | Inspect Yule directly and compare explicit membership lists; retain the intermediary voice. |
| ARC-DIS-002 | CLASSIFICATION | Decorte and Ferrara–Montecchi–Valério present different script/formula models; register-level attribution is not an aligned sign-reading pair. | Locate the exact arguments and selected objects in each publication before evaluating the model. |
| ARC-DIS-003 | INTERPRETATION | Decorte’s seven pattern classes cannot be collapsed into one invariant formula. | Compare object/face occurrences with the authority-specific table before assigning a pattern. |
| ARC-DIS-004 | INTERPRETATION | Decorte and CHIC sign labels are separate models; questioned ASd002=AS013 remains questioned. | Direct graph-level comparison and expert assessment remain open; no phonetic equivalence follows. |
| ARC-AS04-MATERIAL | METADATA_COMPARISON | AS#04 has an explicit INSCRIBE Ivory versus Decorte Table8 Bone material delta. The digital join is not independent physical certification. | Check primary catalogue and material terminology; preserve both authority states. |

`research/attribution-review.json` pins every referenced native artifact by SHA-256 and records exact JSON pointers. `analysis/attribution-review-audit.json` is replayed by the checker. Queries reject changed input bytes before returning any case. The earlier native records remain unchanged.

Pair-attribution states describe documentary limitations, not scientific acceptance. A partial located comparison can be a real scholarly alternative without full typographic, physical-position or independent collation. `NOT_APPLICABLE` marks controls and interpretations for which a two-reading pair is not the appropriate unit. No unknown pair/witness total is replaced with zero.
