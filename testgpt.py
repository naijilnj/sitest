"""
# ---------- 1. Basic Data ----------
x <- c(10, 12, 14, 16, 18)

mean(x)
sd(x)
length(x)

# ---------- 2. Confidence Interval & p-value ----------
t.test(x, conf.level = 0.95)
t.test(x)$p.value

# CI Plot
mean_val <- mean(x)
lower <- 10
upper <- 18

plot(1, mean_val, ylim = c(5, 25),
     pch = 19, main = "Confidence Interval",
     ylab = "Values")
arrows(1, lower, 1, upper,
       angle = 90, code = 3, length = 0.1)

# ---------- 3. Z-Test ----------
mu <- 12
z <- (mean(x) - mu) / (sd(x)/sqrt(length(x)))
z

# Normal Distribution Plot
xv <- seq(-4, 4, length = 100)
yv <- dnorm(xv)

plot(xv, yv, type = "l", lwd = 2,
     main = "Normal Distribution",
     xlab = "Z", ylab = "Density")
abline(v = c(-1.96, 1.96), col = "red", lty = 2)

# ---------- 4. Proportion Test ----------
prop.test(45, 100)

# ---------- 5. t-Test ----------
t.test(x, mu = 12)

# Paired t-test
x1 <- c(10, 12, 14)
y1 <- c(9, 11, 15)

t.test(x1, y1, paired = TRUE)

# t-Distribution Plot
xv <- seq(-4, 4, length = 100)
yv <- dt(xv, df = 10)

plot(xv, yv, type = "l", lwd = 2,
     main = "t Distribution",
     xlab = "t", ylab = "Density")

# ---------- 6. F-Test ----------
x2 <- c(10, 12, 14, 16)
y2 <- c(8, 9, 11, 13)

var.test(x2, y2)

# F-Distribution Plot
xv <- seq(0, 5, length = 100)
yv <- df(xv, df1 = 5, df2 = 10)

plot(xv, yv, type = "l", lwd = 2,
     main = "F Distribution",
     xlab = "Value", ylab = "Density")

# ---------- 7. Chi-Square Tests ----------

# Goodness of Fit
x3 <- c(20, 30, 50)
chisq.test(x3)

# Independence Test
x4 <- c(1,1,2,2,1)
y4 <- c(1,2,1,2,1)

chisq.test(table(x4, y4))

# Chi-Square Plot
xv <- seq(0, 20, length = 100)
yv <- dchisq(xv, df = 5)

plot(xv, yv, type = "l", lwd = 2,
     main = "Chi-Square Distribution",
     xlab = "Value", ylab = "Density")

# ---------- 8. Histogram + Density ----------
x5 <- rnorm(100)

hist(x5, probability = TRUE,
     main = "Histogram",
     xlab = "Values", col = "lightblue")

lines(density(x5), lwd = 2)


"""