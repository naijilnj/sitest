"""

Install.packages(“BSDA”) 
library(BSDA)  
zsum.test(501,112,500,conf.level = 0.95)



A study was conducted in which two types of engines, A and B, were compared. Gas mileage, in 
miles per gallon, was measured. Fifty experiments were conducted using engine type A and 75 
experiments were done with engine type B. The gasoline used and other conditions were held 
constant. The average gas mileage was 36 miles per gallon for engine A and 42miles per gallon for 
engine B. Find a 96%confidence interval on μB−μA, where μA and μB are population mean gas 
mileages for engines A and B, respectively. Assume that the population standard deviations are 6 
and 8 for engines A and B,respectively. 
Code :

zsum.test(42,8,75,36,6,50,mu=0,conf.level = 0.96)


Example 3 
: Two independent sampling stations were chosen for this study, one located downstream from the 
acid mine discharge point and the other located upstream. For 12 monthly samples collected at the 
downstream station, the species diversity index had a mean value deviation = 3.11 and a standard = 
0.771, while 10 monthly samples collected at the upstream station had a mean index value = 2.04 
and a standard deviation = 0.448. Find a 90% confidence interval for the difference between the 
population means for the two locations, assuming that the populations are approximately normally 
distributed with equal variances. 

Code: 
tsum.test(mean.x=3.11,s.x = 0.771,n.x =12 ,mean.y =2.04,s.y =0.448,n.y = 10,var.equal = 
TRUE,conf.level = 0.90)

Example 4: 
A machine produces metal pieces that are cylindrical in shape. A sample of pieces is taken, and the 
diameters are found to be 1.01, 0.97, 1.03, 1.04, 0.99, 0.98, 0.99, 1.01, and 1.03 centimeters. Find a 
99% confidence interval for the mean diameter of pieces from this machine, assuming an 
approximately normal distribution.

Code: 
x<-c(1.01, 0.97, 1.03, 1.04, 0.99, 0.98, 0.99, 1.01,1.03)  
t.test(x,conf.level=0.99)

Example 5  
Simulate 50 samples of size 20 from a normal distribution with mean 100 and standard deviation 5. 
From the 50 simulated samples, construct 95% confidence intervals for the Mean.

Code: 
CIsim( samples = 50, n = 20, mu = 100,sigma = 5, conf.level = 0.95, type = "Mean")


Example 6: 
A study was conducted by the Department of Zoology at the Virginia Tech to estimate the difference 
in the amounts of the chemical orthophosphorus measured at two different stations on the James 
River. Orthophosphorus was measured in milligrams per liter. Fifteen samples were collected from 
station 1, and 12 samples were obtained from station 2. The 15 samples from station 1 had an 
average orthophosphorus content of 3.84 milligrams per liter and a standard deviation of 3.07 
milligrams per liter, while the 12 samples from station 2 had an average content of 1.49 milligrams 
per liter and a standard deviation of 0.80 milligram per liter. Find a 95% confidence interval for the 
difference in the true average orthophosphorus contents at these two stations, assuming that the 
observations came from normal populations with different variances. 
Code: 
tsum.test(mean.x=3.84,s.x =3.07,,n.x =15,mean.y =1.49,s.y =0.8,n.y = 12,var.equal =FALSE, conf.level 
= 0.95)


Example 7  
A certain change in a process for manufacturing component parts is being considered. Samples are 
taken under both the existing and the new process so as to determine if the new process results in 
an improvement. If 75 of 1500 items from the existing process are found to be defective and 80 of 
2000 items from the new process are found to be defective, find a 90% confidence interval for the 
true difference in the proportion of defectives between the existing and the new process. 
Code: 
prop.test(x=c(75,80),n=c(1500,2000),conf.level = 0.90,correct = FALSE)


Example 8  
Two different brands of latex paint are being considered for use. Fifteen specimens of each type of 
paint were selected, and the drying times, in hours, were as follows: 
Paint A: 3.5 , 2.7, 3.9, 4.2, 3.6, 2.7, 3.3, 5.2, 4.2, 2.9, 4.4, 5.2, 4.0, 4.1, 3.4  
Paint B: 4.7, 3.9, 4.5, 5.5, 4.0, 5.3, 4.3, 6.0, 5.2, 3.7, 5.5, 6.2, 5.1, 5.4, 4.8  
Assume the drying time is normally distributed with σA = σB. Find a 95% confidence interval on μB − 
μA, where μA and μB are the mean drying times. 
Code: 
P_A <-c(3.5 , 2.7, 3.9, 4.2, 3.6, 2.7, 3.3, 5.2, 4.2, 2.9, 4.4, 5.2, 4.0, 4.1, 3.4) 

P_B<-c(4.7, 3.9, 4.5, 5.5, 4.0, 5.3, 4.3, 6.0, 5.2, 3.7, 5.5, 6.2, 5.1, 5.4, 4.8)  
t.test(P_B,P_A,paired = FALSE, var.equal =TRUE, conf.level = 0.95)

# p-value  
1. Right tailed test : 
pnorm(q=2.02, lower.tail=FALSE) 
 
2. Left tailed test  
pnorm(q=-0.77, lower.tail=TRUE)  

3.  Two tailed test  
2*pnorm(q=2.83, lower.tail=FALSE)  

4. t-test   --- p-value from t score  
2*pt(q=2.06, 14,lower.tail=FALSE)

"""