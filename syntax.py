###############################
# 1. ONE SAMPLE Z-TEST (MEAN)
###############################
xbar <- 1150
mu0  <- 1200
s    <- 160
n    <- 64
alpha <- 0.05

z <- (xbar - mu0) / (s / sqrt(n))
p_value <- pnorm(z)   # left-tailed

z_crit <- qnorm(alpha)

if (z < z_crit) {
  cat("Reject H0\n")
} else {
  cat("Fail to Reject H0\n")
}


###############################
# 2. TWO SAMPLE Z-TEST (MEAN)
###############################
xbar1 <- 75; xbar2 <- 70
s1 <- 8; s2 <- 9
n1 <- 50; n2 <- 45

z <- (xbar1 - xbar2) / sqrt((s1^2/n1) + (s2^2/n2))
p_value <- 2 * (1 - pnorm(abs(z)))

z_crit <- qnorm(1 - alpha/2)

if (abs(z) > z_crit) {
  cat("Reject H0\n")
} else {
  cat("Fail to Reject H0\n")
}


###############################
# 3. ONE PROPORTION Z-TEST
###############################
x <- 300
n <- 500
p0 <- 0.65

phat <- x/n
z <- (phat - p0) / sqrt(p0*(1-p0)/n)
p_value <- pnorm(z)

z_crit <- qnorm(alpha)

if (z < z_crit) {
  cat("Reject H0\n")
} else {
  cat("Fail to Reject H0\n")
}


###############################
# 4. TWO PROPORTION Z-TEST
###############################
x1 <- 40; n1 <- 400
x2 <- 70; n2 <- 350

p1 <- x1/n1
p2 <- x2/n2
p  <- (x1+x2)/(n1+n2)

z <- (p1 - p2) / sqrt(p*(1-p)*(1/n1 + 1/n2))
p_value <- 2 * (1 - pnorm(abs(z)))

z_crit <- qnorm(1 - alpha/2)

if (abs(z) > z_crit) {
  cat("Reject H0\n")
} else {
  cat("Fail to Reject H0\n")
}


###############################
# 5. ONE SAMPLE t-TEST
###############################
x <- rnorm(20, mean=50, sd=10)
t.test(x, mu=50, alternative="two.sided")


###############################
# 6. PAIRED t-TEST
###############################
before <- c(10,12,11,14,13)
after  <- c(12,13,12,15,14)

t.test(before, after, paired=TRUE)


###############################
# 7. CHI-SQUARE GOODNESS OF FIT
###############################
obs <- c(10,18,20,22,25,25)
exp <- rep(sum(obs)/6, 6)

chi_cal <- sum((obs - exp)^2 / exp)
df <- length(obs) - 1

chi_crit <- qchisq(1 - alpha, df)

if (chi_cal > chi_crit) {
  cat("Reject H0\n")
} else {
  cat("Fail to Reject H0\n")
}


###############################
# 8. CHI-SQUARE TEST (INDEPENDENCE)
###############################
data1 <- matrix(c(30,120,60,90), nrow=2, byrow=TRUE)

test <- chisq.test(data1, correct=FALSE)
test

if (test$p.value < alpha) {
  cat("Reject H0\n")
} else {
  cat("Fail to Reject H0\n")
}


###############################
# 9. F-TEST (VARIANCE EQUALITY)
###############################
s1_sq <- 36
s2_sq <- 16
n1 <- 15
n2 <- 18

f_cal <- s1_sq / s2_sq

df1 <- n1 - 1
df2 <- n2 - 1

f_upper <- qf(1 - alpha/2, df1, df2)
f_lower <- 1 / qf(1 - alpha/2, df2, df1)

if (f_cal < f_lower || f_cal > f_upper) {
  cat("Reject H0\n")
} else {
  cat("Fail to Reject H0\n")
}


###############################
# 10. F-TEST (ONE-TAILED)
###############################
s1_sq <- 40
s2_sq <- 20
n1 <- 14
n2 <- 16

f_cal <- s1_sq / s2_sq

df1 <- n1 - 1
df2 <- n2 - 1

f_crit <- qf(1 - alpha, df1, df2)

if (f_cal > f_crit) {
  cat("Reject H0\n")
} else {
  cat("Fail to Reject H0\n")
}


############################################################
# PLOTTING TEMPLATES
############################################################

# Z Distribution
z_vals <- seq(-4,4,length=1000)
plot(z_vals, dnorm(z_vals), type='l')

# Chi-square Distribution
x <- seq(0,10,length=1000)
plot(x, dchisq(x, df=2), type='l')

# F Distribution
x <- seq(0,5,length=1000)
plot(x, df(x, df1=5, df2=10), type='l')