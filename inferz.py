"""
Q1) A manufacturer claims that the average lifetime of batteries is 1200 hours.
A random sample of n = 64 batteries shows a mean lifetime of 1150 hours with a sample
standard deviation of 160 hours. At 5% level of significance, test whether the mean lifetime is
less than claimed.

Code:

# Given data
xbar <- 1150
mu0 <- 1200
s <- 160
n <- 64

# Z-test statistic
z <- (xbar - mu0) / (s / sqrt(n))
z

# p-value (left-tailed)
pnorm(z)

# t-test (simulation)
x <- rnorm(64, mean = 1150, sd = 160)
t.test(x, mu = 1200, alternative = "less")

# Plot
z_vals <- seq(-4, 1, length = 1000)
dens <- dnorm(z_vals)

plot(z_vals, dens, type='l', lwd=2,
     main="One Sample Z Test (Left-Tailed)",
     xlab="Z", ylab="Density")

z_crit <- -1.645
z_left <- z_vals[z_vals <= z_crit]
dens_left <- dnorm(z_left)

polygon(c(z_left, rev(z_left)),
        c(dens_left, rep(0, length(dens_left))),
        col="red", border=NA)

abline(v = z, col="blue", lwd=2)

legend("topright",
       legend=c("Critical region", "Observed Z"),
       fill=c("red", NA),
       border=c(NA, NA),
       lwd=c(NA, 2),
       col=c(NA, "blue"))

# Decision
if (z < z_crit) {
  cat("Mean lifetime is less than claimed")
} else {
  cat("No evidence that mean is less than claimed")
}

Q2) Two Sample Z-Test (Means)
Question

Compare two teaching methods:

Method	n	Mean	SD
A	    50	75	    8
B	    45	70	    9

Test at 5% significance if there is a difference.

Code:

# Data
xbar1 <- 75; xbar2 <- 70
s1 <- 8; s2 <- 9
n1 <- 50; n2 <- 45

# Z statistic
z <- (xbar1 - xbar2) / sqrt((s1^2/n1) + (s2^2/n2))
z

# Two-tailed p-value
2 * (1 - pnorm(abs(z)))

# t-test (simulation)
x1 <- rnorm(50, mean = 75, sd = 8)
x2 <- rnorm(45, mean = 70, sd = 9)
t.test(x1, x2, alternative = "two.sided")

# Plot
z_vals <- seq(-4, 4, length = 1000)
dens <- dnorm(z_vals)

plot(z_vals, dens, type='l', lwd=2,
     main="Two Sample Z Test",
     xlab="Z", ylab="Density")

z_crit <- 1.96

# Left region
z_left <- z_vals[z_vals <= -z_crit]
polygon(c(z_left, rev(z_left)),
        c(dnorm(z_left), rep(0, length(z_left))),
        col="lightcoral", border=NA)

# Right region
z_right <- z_vals[z_vals >= z_crit]
polygon(c(z_right, rev(z_right)),
        c(dnorm(z_right), rep(0, length(z_right))),
        col="lightcoral", border=NA)

abline(v = z, col="blue", lwd=2)

legend("topright",
       legend=c("Critical region", "Observed Z"),
       fill=c("lightcoral", NA),
       border=c(NA, NA),
       lwd=c(NA, 2),
       col=c(NA, "blue"))

# Decision
if (abs(z) > z_crit) {
  cat("Significant difference exists")
} else {
  cat("No significant difference")
}



Q3) Two Proportion Z-Test
Question

Factory data:

Factory	n	Defective
A	400	40
B	350	70

Test if defective proportions differ.

Code:

# Data
x1 <- 40; n1 <- 400
x2 <- 70; n2 <- 350

p1 <- x1 / n1
p2 <- x2 / n2

# Pooled proportion
p_pool <- (x1 + x2) / (n1 + n2)

# Z statistic
z <- (p1 - p2) / sqrt(p_pool * (1 - p_pool) * (1/n1 + 1/n2))
z

# p-value
2 * (1 - pnorm(abs(z)))

# Plot
z_vals <- seq(-4, 4, length = 1000)
dens <- dnorm(z_vals)

plot(z_vals, dens, type='l', lwd=2,
     main="Two Proportion Z Test",
     xlab="Z", ylab="Density")

z_crit <- 1.96

# Shade regions
z_left <- z_vals[z_vals <= -z_crit]
polygon(c(z_left, rev(z_left)),
        c(dnorm(z_left), rep(0, length(z_left))),
        col="pink", border=NA)

z_right <- z_vals[z_vals >= z_crit]
polygon(c(z_right, rev(z_right)),
        c(dnorm(z_right), rep(0, length(z_right))),
        col="pink", border=NA)

abline(v = z, col="blue", lwd=2)

legend("topright",
       legend=c("Critical region", "Observed Z"),
       fill=c("pink", NA),
       border=c(NA, NA),
       lwd=c(NA, 2),
       col=c(NA, "blue"))

# Decision
if (abs(z) > z_crit) {
  cat("Proportions differ")
} else {
  cat("No significant difference")
}



Q4) One Proportion Z-Test (Left-Tailed)
Question

Company claims 65% satisfaction.
Sample: 500 customers, 300 satisfied.

Test if true proportion is less than 0.65.

Code

# Data
x <- 300
n <- 500
p0 <- 0.65

phat <- x / n

# Z statistic
z <- (phat - p0) / sqrt(p0 * (1 - p0) / n)
z

# p-value
pnorm(z)

# Plot
z_vals <- seq(-4, 4, length = 1000)
dens <- dnorm(z_vals)

plot(z_vals, dens, type='l', lwd=2,
     main="One Proportion Z Test (Left-Tailed)",
     xlab="Z", ylab="Density")

z_crit <- -1.645

z_left <- z_vals[z_vals <= z_crit]
polygon(c(z_left, rev(z_left)),
        c(dnorm(z_left), rep(0, length(z_left))),
        col="green", border=NA)

abline(v = z, col="blue", lwd=2)

legend("topright",
       legend=c("Critical region", "Observed Z"),
       fill=c("green", NA),
       border=c(NA, NA),
       lwd=c(NA, 2),
       col=c(NA, "blue"))

# Decision
if (z < z_crit) {
  cat("True proportion is less than 0.65")
} else {
  cat("No evidence that proportion is less than 0.65")
}
"""