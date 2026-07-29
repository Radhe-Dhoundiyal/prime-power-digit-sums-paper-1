# Table 1 Validation

New values use `len(str(power))` as the authoritative digit count.
The manuscript supplies six displayed decimal places; no higher-precision
manuscript values are available for a full-precision equality comparison.

| Prime | N | Computed full precision | Computed 6 d.p. | Manuscript | 6 d.p. status |
|---:|---:|---:|---:|---:|---|
| 2 | 50 | 1.1331725844490292 | 1.133173 | 1.133173 | PASS |
| 2 | 250 | 0.62978602838350672 | 0.629786 | 0.629786 | PASS |
| 2 | 500 | 0.48079499548006099 | 0.480795 | 0.480795 | PASS |
| 2 | 1000 | 0.36571435513836997 | 0.365714 | 0.365714 | PASS |
| 2 | 2000 | 0.27515012238177278 | 0.275150 | 0.275150 | PASS |
| 2 | 4000 | 0.20646928980102169 | 0.206469 | 0.206469 | PASS |
| 2 | 8000 | 0.15422948432249264 | 0.154229 | 0.154229 | PASS |
| 101 | 50 | 1.0703908437459666 | 1.070391 | 1.070391 | PASS |
| 101 | 250 | 0.57755508226229957 | 0.577555 | 0.577555 | PASS |
| 101 | 500 | 0.42037584702870129 | 0.420376 | 0.420376 | PASS |
| 101 | 1000 | 0.30426580328355257 | 0.304266 | 0.304266 | PASS |
| 101 | 2000 | 0.21956201422374244 | 0.219562 | 0.219562 | PASS |
| 101 | 4000 | 0.15794824043021954 | 0.157948 | 0.157948 | PASS |
| 101 | 8000 | 0.11342863504248116 | 0.113429 | 0.113429 | PASS |
| 197 | 50 | 0.46780400777833298 | 0.467804 | 0.467804 | PASS |
| 197 | 250 | 0.26058583030459304 | 0.260586 | 0.260586 | PASS |
| 197 | 500 | 0.1978702609227839 | 0.197870 | 0.197870 | PASS |
| 197 | 1000 | 0.14815771278765821 | 0.148158 | 0.148158 | PASS |
| 197 | 2000 | 0.11034941636178482 | 0.110349 | 0.110349 | PASS |
| 197 | 4000 | 0.082032488547893953 | 0.082032 | 0.082032 | PASS |
| 197 | 8000 | 0.060665310632480172 | 0.060665 | 0.060665 | PASS |

**Overall six-decimal result: PASS.**

Full-precision comparison status: **NOT POSSIBLE** because the manuscript
prints only six decimals. Full computed precision is retained above and in CSV.
