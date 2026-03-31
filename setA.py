"""
# ==========================================
# Q1: CHI-SQUARE TEST (FAIR DIE)
# ==========================================

# Observed frequencies
obs <- c(14, 18, 20, 22, 24, 22)

# Expected frequencies (fair die)
exp <- rep(20, 6)

# Hypothesis:
# H0: Die is fair
# H1: Die is not fair

# Chi-square test
chi_test <- chisq.test(obs)
print(chi_test)

# Test statistic (manual)
chi_stat <- sum((obs - exp)^2 / exp)
print(paste("Chi-square statistic =", chi_stat))

# p-value
p_val <- pchisq(chi_stat, df = 5, lower.tail = FALSE)
print(paste("p-value =", p_val))

# Conclusion
if (p_val < 0.05) {
  print("Reject H0: Die is not fair")
} else {
  print("Fail to reject H0: Die is fair")
}


# -------- Plot: Bar Chart (Observed vs Expected) --------
barplot(rbind(obs, exp),
        beside = TRUE,
        col = c("blue", "red"),
        legend.text = c("Observed", "Expected"),
        main = "Observed vs Expected Frequencies",
        xlab = "Die Faces",
        ylab = "Frequency")


# -------- Plot: Chi-square Distribution --------
x <- seq(0, 15, length = 100)
y <- dchisq(x, df = 5)

plot(x, y, type = "l", lwd = 2,
     main = "Chi-square Distribution (df = 5)",
     xlab = "Chi-square value",
     ylab = "Density")

# Shade rejection region (right tail)
critical_value <- qchisq(0.95, df = 5)
polygon(c(critical_value, x[x >= critical_value], max(x)),
        c(0, y[x >= critical_value], 0),
        col = "red")

# Mark observed statistic
abline(v = chi_stat, col = "blue", lwd = 2)



# ==========================================
# Q2: F-TEST (VARIANCE COMPARISON)
# ==========================================

# Given values
n1 <- 12
n2 <- 10
s1_sq <- 18.5
s2_sq <- 42.0

# Hypothesis:
# H0: sigma1^2 = sigma2^2
# H1: sigma1^2 < sigma2^2 (Machine A more consistent)

# F-statistic
F_stat <- s1_sq / s2_sq
print(paste("F-statistic =", F_stat))

# Degrees of freedom
df1 <- n1 - 1
df2 <- n2 - 1

# p-value (left-tailed test)
p_val_F <- pf(F_stat, df1 = df1, df2 = df2)
print(paste("p-value =", p_val_F))

# Decision at alpha = 0.01
if (p_val_F < 0.01) {
  print("Reject H0 at 1% level")
} else {
  print("Fail to reject H0 at 1% level")
}

# Decision at alpha = 0.05
if (p_val_F < 0.05) {
  print("Reject H0 at 5% level")
} else {
  print("Fail to reject H0 at 5% level")
}


# -------- Plot: F Distribution --------
x <- seq(0, 3, length = 100)
y <- df(x, df1 = df1, df2 = df2)

plot(x, y, type = "l", lwd = 2,
     main = "F Distribution",
     xlab = "F value",
     ylab = "Density")

# Shade rejection region (left tail)
critical_F <- qf(0.01, df1, df2)
polygon(c(0, x[x <= critical_F], critical_F),
        c(0, y[x <= critical_F], 0),
        col = "red")

# Mark observed F-statistic
abline(v = F_stat, col = "blue", lwd = 2)


"""