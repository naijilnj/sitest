"""
Two independent random samples are taken from two normal populations:

Sample 1:

n1=15, s12=36
n2=18, s22=16

Test at 5% level of significance whether the population variances are equal.


# Given data
s1_sq <- 36
s2_sq <- 16
n1 <- 15
n2 <- 18
alpha <- 0.05

# F statistic
f_cal <- s1_sq / s2_sq
f_cal

# Degrees of freedom
df1 <- n1 - 1
df2 <- n2 - 1

# Critical values (two-tailed)
f_upper <- qf(1 - alpha/2, df1, df2)
f_lower <- 1 / qf(1 - alpha/2, df2, df1)

f_upper
f_lower

# Plot
x <- seq(0, 6, length = 1000)
y <- df(x, df1, df2)

plot(x, y, type = 'l', lwd = 2,
     main = "F Distribution (Two-Tailed Test)",
     xlab = "F value", ylab = "Density")

# Left rejection region
x_left <- seq(0, f_lower, length = 500)
polygon(c(0, x_left, f_lower),
        c(0, df(x_left, df1, df2), 0),
        col = "red", border = NA)

# Right rejection region
x_right <- seq(f_upper, 6, length = 500)
polygon(c(f_upper, x_right, 6),
        c(0, df(x_right, df1, df2), 0),
        col = "red", border = NA)

# Lines
abline(v = f_lower, lty = 2, lwd = 2)
abline(v = f_upper, lty = 2, lwd = 2)
abline(v = f_cal, col = "blue", lwd = 2)

# Decision
if (f_cal < f_lower || f_cal > f_upper) {
  cat("Reject H0: Variances are not equal")
} else {
  cat("Fail to Reject H0: Variances may be equal")
}


Q2) F-Test (One-Tailed – Larger Variance)
Question

Two independent samples:
n1=14, s12=40
n2=16, s22=20


Code)

# Given data
s1_sq <- 40
s2_sq <- 20
n1 <- 14
n2 <- 16
alpha <- 0.05

# F statistic
f_cal <- s1_sq / s2_sq
f_cal

# Degrees of freedom
df1 <- n1 - 1
df2 <- n2 - 1

# Critical value (right-tailed)
f_critical <- qf(1 - alpha, df1, df2)
f_critical

# Plot
x <- seq(0, 6, length = 1000)
y <- df(x, df1, df2)

plot(x, y, type = 'l', lwd = 2,
     main = "F Distribution (One-Tailed Test)",
     xlab = "F value", ylab = "Density")

# Right rejection region
x_right <- seq(f_critical, 6, length = 500)
polygon(c(f_critical, x_right, 6),
        c(0, df(x_right, df1, df2), 0),
        col = "orange", border = NA)

# Lines
abline(v = f_critical, lty = 2, lwd = 2)
abline(v = f_cal, col = "green", lwd = 2)

# Decision
if (f_cal > f_critical) {
  cat("Reject H0: Population 1 has larger variance")
} else {
  cat("Fail to Reject H0: No evidence that variance is larger")
}



"""