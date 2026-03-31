STATISTICS FORMULA SHEET (ALL TESTS)

--------------------------------------------------
1. CONFIDENCE INTERVAL

Mean (sigma known):
xbar ± Z * (sigma / sqrt(n))

Mean (sigma unknown):
xbar ± t * (s / sqrt(n))

Proportion:
phat ± Z * sqrt( phat * (1 - phat) / n )

--------------------------------------------------
2. ONE SAMPLE Z-TEST (MEAN)

Z = (xbar - mu0) / (s / sqrt(n))

--------------------------------------------------
3. TWO SAMPLE Z-TEST (MEANS)

Z = (xbar1 - xbar2) / sqrt( (s1^2 / n1) + (s2^2 / n2) )

--------------------------------------------------
4. ONE PROPORTION Z-TEST

Z = (phat - p0) / sqrt( p0 * (1 - p0) / n )

--------------------------------------------------
5. TWO PROPORTION Z-TEST

Z = (p1 - p2) / sqrt( p * (1 - p) * (1/n1 + 1/n2) )

where:
p = (x1 + x2) / (n1 + n2)

--------------------------------------------------
6. T-TEST (ONE SAMPLE)

t = (xbar - mu0) / (s / sqrt(n))

--------------------------------------------------
7. PAIRED T-TEST

t = dbar / (sd / sqrt(n))

where:
dbar = mean of differences
sd   = standard deviation of differences

--------------------------------------------------
8. F-TEST (VARIANCE TEST)

F = s1^2 / s2^2

df1 = n1 - 1
df2 = n2 - 1

--------------------------------------------------
9. CHI-SQUARE TEST (GOODNESS OF FIT)

chi-square = sum( (O - E)^2 / E )

--------------------------------------------------
10. CHI-SQUARE TEST (INDEPENDENCE)

chi-square = sum( (O - E)^2 / E )

Expected value:
E = (Row Total * Column Total) / Grand Total

--------------------------------------------------
11. P-VALUE

Left-tailed:
p = P(Z < z)

Right-tailed:
p = P(Z > z)

Two-tailed:
p = 2 * P(Z > |z|)

--------------------------------------------------
12. CRITICAL VALUES

Z-values:
5% two-tailed  = ±1.96
5% one-tailed  = 1.645

t-values:
depends on df = n - 1

Chi-square:
chi-square(alpha, df)

F-test:
F(alpha, df1, df2)

--------------------------------------------------
WHICH TEST TO USE

Mean (large sample)        -> Z-test
Mean (small sample)        -> t-test
Two means                  -> Z / t
Proportion                 -> Z-test
Two proportions            -> Z-test
Variance comparison        -> F-test
Observed vs expected       -> Chi-square
Relationship (categories)  -> Chi-square (independence)

--------------------------------------------------
END