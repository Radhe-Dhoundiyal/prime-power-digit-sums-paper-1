# Normalization Notes

The authoritative statistic is

$$
\widetilde A_p(n)=\frac{S(p^n)}{\ell_p(n)},\qquad
\ell_p(n)=\lfloor n\log_{10}p\rfloor+1.
$$

The implementation authority for $\ell_p(n)$ is decimal string length. The
logarithmic expression remains the mathematical definition and is evaluated
independently for every observation.

The older approximation

$$
A_p(n)=\frac{S(p^n)}{n\log_{10}p}
$$

is supplementary only. It must not be substituted for the exact statistic in
Table 1 or Figures 1-4. This repository does not publish the older standalone
approximate plots because their source provenance was not retained.
