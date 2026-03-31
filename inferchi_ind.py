"""


Q1: Chi-Square Test of Independence (Exercise vs Heart Disease)
Question

A study was conducted to examine whether exercise habits are related to heart disease.

	Heart Disease	No Heart Disease	Total
Regular Exercise	30	120	150
No Exercise	60	90	150
Total	90	210	300

At 5% level of significance, test whether exercise and heart disease are independent.


# Data matrix
data1 <- matrix(c(30, 120, 60, 90), nrow = 2, byrow = TRUE)

rownames(data1) <- c("Regular Exercise", "No Exercise")
colnames(data1) <- c("Heart Disease", "No Heart Disease")

data1

# Chi-square test
test1 <- chisq.test(data1, correct = FALSE)
test1

# Critical value method
df1 <- test1$parameter
alpha <- 0.05
critical1 <- qchisq(1 - alpha, df1)

cat("Critical Value =", critical1, "\n")

# Decision
if (test1$statistic > critical1) {
  cat("Reject H0: Variables are dependent\n")
} else {
  cat("Fail to Reject H0: Variables are independent\n")
}

# Bar plot
barplot(data1,
        beside = TRUE,
        col = c("steelblue", "tomato"),
        legend = rownames(data1),
        main = "Exercise Habits vs Heart Disease",
        ylab = "Frequency")

# Mosaic plot
mosaicplot(data1,
           color = TRUE,
           main = "Exercise Habits and Heart Disease")

# Association plot
assocplot(data1,
          main = "Association Plot: Exercise vs Heart Disease")


Q2: Chi-Square Test of Independence (Junk Food vs Obesity)
Question

A study was conducted to examine whether junk food consumption is related to obesity.

	Obese	Not Obese	Total
Regular Junk Food	70	80	150
Rarely Junk Food	30	70	100
Total	100	150	250

At 5% level of significance, test whether junk food consumption and obesity are independent.


# Data matrix
data1 <- matrix(c(70, 80, 30, 70), nrow = 2, byrow = TRUE)

rownames(data1) <- c("Regular Junk Food", "Rarely Junk Food")
colnames(data1) <- c("Obese", "Not Obese")

data1

# Chi-square test
test1 <- chisq.test(data1, correct = FALSE)
test1

# Critical value method
df1 <- test1$parameter
alpha <- 0.05
critical1 <- qchisq(1 - alpha, df1)

cat("Critical Value =", critical1, "\n")

# Decision
if (test1$statistic > critical1) {
  cat("Reject H0: Variables are dependent\n")
} else {
  cat("Fail to Reject H0: Variables are independent\n")
}

# Bar plot
barplot(data1,
        beside = TRUE,
        col = c("pink", "green"),
        legend = rownames(data1),
        main = "Junk Food Consumption vs Obesity",
        ylab = "Frequency")

# Mosaic plot
mosaicplot(data1,
           color = TRUE,
           main = "Junk Food Consumption vs Obesity")

# Association plot
assocplot(data1,
          main = "Association Plot: Junk Food vs Obesity")

          
"""