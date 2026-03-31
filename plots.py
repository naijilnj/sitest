"""

############################################################
# 1. ONE SAMPLE Z TEST (LEFT-TAILED)
############################################################
z_vals <- seq(-4, 4, length = 1000)
dens <- dnorm(z_vals)

z <- -2        # replace with your value
z_crit <- -1.645

plot(z_vals, dens, type='l', lwd=2,
     main="One Sample Z Test (Left-Tailed)",
     xlab="Z", ylab="Density")

z_left <- z_vals[z_vals <= z_crit]
polygon(c(z_left, rev(z_left)),
        c(dnorm(z_left), rep(0, length(z_left))),
        col="red", border=NA)

abline(v = z_crit, lty=2, lwd=2)
abline(v = z, col="blue", lwd=2)


############################################################
# 2. TWO SAMPLE Z TEST (TWO-TAILED)
############################################################
z_vals <- seq(-4, 4, length = 1000)
dens <- dnorm(z_vals)

z <- 2.1       # replace with your value
z_crit <- 1.96

plot(z_vals, dens, type='l', lwd=2,
     main="Two Sample Z Test",
     xlab="Z", ylab="Density")

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

abline(v = -z_crit, lty=2)
abline(v = z_crit, lty=2)
abline(v = z, col="blue", lwd=2)


############################################################
# 3. TWO PROPORTION Z TEST
############################################################
z_vals <- seq(-4, 4, length = 1000)
dens <- dnorm(z_vals)

z <- -3.8      # replace with your value
z_crit <- 1.96

plot(z_vals, dens, type='l', lwd=2,
     main="Two Proportion Z Test",
     xlab="Z", ylab="Density")

z_left <- z_vals[z_vals <= -z_crit]
polygon(c(z_left, rev(z_left)),
        c(dnorm(z_left), rep(0, length(z_left))),
        col="pink", border=NA)

z_right <- z_vals[z_vals >= z_crit]
polygon(c(z_right, rev(z_right)),
        c(dnorm(z_right), rep(0, length(z_right))),
        col="pink", border=NA)

abline(v = -z_crit, lty=2)
abline(v = z_crit, lty=2)
abline(v = z, col="blue", lwd=2)


############################################################
# 4. ONE PROPORTION Z TEST (LEFT-TAILED)
############################################################
z_vals <- seq(-4, 4, length = 1000)
dens <- dnorm(z_vals)

z <- -2.34     # replace with your value
z_crit <- -1.645

plot(z_vals, dens, type='l', lwd=2,
     main="One Proportion Z Test",
     xlab="Z", ylab="Density")

z_left <- z_vals[z_vals <= z_crit]
polygon(c(z_left, rev(z_left)),
        c(dnorm(z_left), rep(0, length(z_left))),
        col="green", border=NA)

abline(v = z_crit, lty=2)
abline(v = z, col="blue", lwd=2)


############################################################
# 5. CHI-SQUARE GOODNESS OF FIT
############################################################
df <- 5
chi_cal <- 7.9
chi_critical <- qchisq(0.95, df)

x <- seq(0, 20, length = 1000)
y <- dchisq(x, df)

plot(x, y, type="l", lwd=2,
     main="Chi-Square Distribution",
     xlab="Chi-square value", ylab="Density")

x_shade <- seq(chi_critical, 20, length=500)
polygon(c(chi_critical, x_shade, 20),
        c(0, dchisq(x_shade, df), 0),
        col="red", border=NA)

abline(v=chi_critical, lty=2)
abline(v=chi_cal, col="blue", lwd=2)


############################################################
# 6. CHI-SQUARE (COIN TEST)
############################################################
df <- 1
chi_cal <- 8
chi_critical <- qchisq(0.95, df)

x <- seq(0, 10, length = 1000)
y <- dchisq(x, df)

plot(x, y, type="l", lwd=2,
     main="Chi-Square Coin Test",
     xlab="Chi-square value", ylab="Density")

x_shade <- seq(chi_critical, 10, length=500)
polygon(c(chi_critical, x_shade, 10),
        c(0, dchisq(x_shade, df), 0),
        col="orange", border=NA)

abline(v=chi_critical, lty=2)
abline(v=chi_cal, col="blue", lwd=2)


############################################################
# 7. F TEST (TWO-TAILED)
############################################################
df1 <- 14
df2 <- 17
f_cal <- 2.25

f_upper <- qf(0.975, df1, df2)
f_lower <- 1 / qf(0.975, df2, df1)

x <- seq(0, 6, length = 1000)
y <- df(x, df1, df2)

plot(x, y, type='l', lwd=2,
     main="F Distribution (Two-Tailed)",
     xlab="F value", ylab="Density")

# Left region
x_left <- seq(0, f_lower, length=500)
polygon(c(0, x_left, f_lower),
        c(0, df(x_left, df1, df2), 0),
        col="red", border=NA)

# Right region
x_right <- seq(f_upper, 6, length=500)
polygon(c(f_upper, x_right, 6),
        c(0, df(x_right, df1, df2), 0),
        col="red", border=NA)

abline(v=f_lower, lty=2)
abline(v=f_upper, lty=2)
abline(v=f_cal, col="blue", lwd=2)


############################################################
# 8. F TEST (ONE-TAILED)
############################################################
df1 <- 13
df2 <- 15
f_cal <- 2

f_critical <- qf(0.95, df1, df2)

x <- seq(0, 6, length = 1000)
y <- df(x, df1, df2)

plot(x, y, type='l', lwd=2,
     main="F Distribution (One-Tailed)",
     xlab="F value", ylab="Density")

x_right <- seq(f_critical, 6, length=500)
polygon(c(f_critical, x_right, 6),
        c(0, df(x_right, df1, df2), 0),
        col="orange", border=NA)

abline(v=f_critical, lty=2)
abline(v=f_cal, col="green", lwd=2)


############################################################
# 9. BAR + MOSAIC + ASSOCIATION (TEMPLATE)
############################################################
data1 <- matrix(c(30,120,60,90), nrow=2, byrow=TRUE)

barplot(data1,
        beside=TRUE,
        col=c("steelblue","tomato"),
        legend=TRUE,
        main="Bar Plot",
        ylab="Frequency")

mosaicplot(data1,
           color=TRUE,
           main="Mosaic Plot")

assocplot(data1,
          main="Association Plot")


"""