"""
> summary(cars)
x<-c("A","B","C","D","E","F")
y<-c(2,4,6,8,10,3)

#Bar plot
barplot(y,names.arg=x,col='thistle')
barplot(table(mtcars$cyl),main = "No. of cylinders",col = 'yellow')

#Box plot
boxplot(mtcars$mpg, col= "pink")

data(mtcars)
boxplot(mpg ~ gear, data = mtcars,
+ col = c("mistyrose", "lightpink", "palevioletred"),
+ xlab = "Number of Gears",
+ ylab = "Miles per Gallon")

#Histogram
hist(mtcars$mpg, col="lightblue")

hist(mtcars$mpg, col="maroon", breaks = 10, border= "white")

den=density(mtcars$mpg)
plot(den, col= "orange",lwd = 2)


#Pie chart
pie(table(mtcars$gear), main="Gears", radius=1,col.main="brown")

#Iris Data
summary(iris)

#Histogram
hist(iris$Sepal.Length, col = "plum")
hist(iris$Sepal.Width, col = "rosybrown1")
hist(iris$Petal.Length, col = "slateblue4")
hist(iris$Petal.Width, col = "salmon")

#Box plot
boxplot(iris$Sepal.Length, col = "plum")
boxplot(iris$Sepal.Width, col = "rosybrown1")
boxplot(iris$Petal.Length, col = "slateblue4")
boxplot(iris$Petal.Width, col = "salmon")

#Pie chart
pie(table(iris$Species), main = "irisspecies", radius=1,
+ col = c('salmon','bisque','burlywood'))

#Scatter plot
plot(iris$Sepal.Length,iris$Sepal.Width,
+ col = iris$Species,pch = 15,
+ xlab = "Sepal Length", ylab = "Sepal Width",
+ main = "Scatterplot of Sepal Dimensions")

#Air Quality Dataset
data("airquality")
summary(airquality)

#Histogram
hist(airquality$Ozone, col = "plum")
hist(airquality$Solar, col = "rosybrown1")
hist(airquality$Wind, col = "slateblue")
hist(airquality$Temp, col = "salmon")
hist(airquality$Month, col = "seashell")
hist(airquality$Day, col = "wheat")

#Boxplot
boxplot(airquality$Ozone, col = "plum")
boxplot(airquality$Solar, col = "rosybrown1")
boxplot(airquality$Wind, col = "slateblue")
boxplot(airquality$Temp, col = "salmon")
boxplot(airquality$Month, col = "seashell")
boxplot(airquality$Day, col = "cadetblue")

# Frequency of each month
month_freq <- table(airquality$Month)

# Pie chart of observations by month
pie(month_freq,
+ main = "Pie Chart of Observations by Month",
+ col = rainbow(length(month_freq)))

# Scatter plot between Ozone and Temperature
plot(airquality$Temp, airquality$Ozone,
+ main = "Scatter Plot of Ozone vs Temperature",
+ xlab = "Temperature (F)",
+ ylab = "Ozone (ppb)",
+ pch = 19,
+ col = "lightblue")


"""