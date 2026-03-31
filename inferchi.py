"""

Q1: Chi-Square Goodness of Fit (Die)
Question

A die is thrown 120 times. The observed frequencies are:

Outcome	1	2	3	4	5	6
Obs	    10	18	20	22	25	25

Test at 5% level of significance whether the die is fair.


# Observed values
obs <- c(10, 18, 20, 22, 25, 25)

# Expected values (fair die)
exp <- rep(120/6, 6)

# Chi-square statistic
chi_cal <- sum((obs - exp)^2 / exp)
chi_cal

# Degrees of freedom
df <- length(obs) - 1

# Critical value
alpha <- 0.05
chi_critical <- qchisq(1 - alpha, df)
chi_critical

# Decision
if (chi_cal > chi_critical) {
  cat("Reject H0: Die is not fair")
} else {
  cat("Fail to Reject H0: Die may be fair")
}

# Plot
x <- seq(0, 20, length = 1000)
y <- dchisq(x, df)

plot(x, y, type = "l", lwd = 2,
     main = "Chi-Square Distribution (Goodness of Fit)",
     xlab = "Chi-square value",
     ylab = "Density")

# Rejection region
x_shade <- seq(chi_critical, 20, length = 500)
y_shade <- dchisq(x_shade, df)

polygon(c(chi_critical, x_shade, 20),
        c(0, y_shade, 0),
        col = "red", border = NA)

# Lines
abline(v = chi_critical, lty = 2, lwd = 2)
abline(v = chi_cal, col = "blue", lwd = 2)

legend("topright",
       legend = c("Critical region", "Observed Chi-square"),
       fill = c("red", NA),
       border = c(NA, NA),
       lwd = c(NA, 2),
       col = c(NA, "blue"))


Q2: Chi-Square Test (Coin Fairness)
Question

A coin is tossed 200 times.

Outcome	Heads	Tails
Obs  	120	    80

Test at 5% level of significance whether the coin is fair.



# Observed values
obs <- c(120, 80)

# Expected values (fair coin)
exp <- rep(200/2, 2)

# Chi-square statistic
chi_cal <- sum((obs - exp)^2 / exp)
chi_cal

# Degrees of freedom
df <- length(obs) - 1

# Critical value
alpha <- 0.05
chi_critical <- qchisq(1 - alpha, df)
chi_critical

# Decision
if (chi_cal > chi_critical) {
  cat("Reject H0: Coin is not fair")
} else {
  cat("Fail to Reject H0: Coin may be fair")
}

# Plot
x <- seq(0, 10, length = 1000)
y <- dchisq(x, df)

plot(x, y, type = "l", lwd = 2,
     main = "Chi-Square Distribution (Coin Test)",
     xlab = "Chi-square value",
     ylab = "Density")

# Rejection region
x_shade <- seq(chi_critical, 10, length = 500)
y_shade <- dchisq(x_shade, df)

polygon(c(chi_critical, x_shade, 10),
        c(0, y_shade, 0),
        col = "orange", border = NA)

# Lines
abline(v = chi_critical, lty = 2, lwd = 2)
abline(v = chi_cal, col = "blue", lwd = 2)

legend("topright",
       legend = c("Critical region", "Observed Chi-square"),
       fill = c("orange", NA),
       border = c(NA, NA),
       lwd = c(NA, 2),
       col = c(NA, "blue"))


"""