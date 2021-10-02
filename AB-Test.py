import pandas as pd
import numpy as np
import scipy.stats as stat

# clicks.csv include site visitors data for a week
abdata = pd.read_csv('clicks.csv')
sig_threshold = 0.05


# test whether visitors are more likely to make a purchase if they are in any one group compared to the others
# Chi-Square test
Xtab = pd.crosstab(abdata.group, abdata.is_purchase)
print(Xtab)
chi2, pval, dof, expected = stat.chi2_contingency(Xtab)
result = ('There is a significant difference in purchase rates for groups A, B and C - \
an association between purchase-status and the group the visitor is in' if pval < sig_threshold \
else 'There is NO significant difference in purchase rate for groups A, B and C')
print(result, 'p-value =', pval)


# the number of visitors to the site in a week
num_visits = len(abdata)
print('Number of site visitors per week:')
print(num_visits)


# calculate the number of visitors who would need to purchase the upgrade package
# at each price point (group A: $0.99,group B: $1.99,group C: $4.99)
# in order to generate a minimum revenue target of $1,000 per week

# for price point $0.99
# the number of sales that would be 'needed' to reach $1,000 of revenue
num_sales_needed_099 = 1000/0.99
print('Number of sales needed to reach $1,000 revenue at price point $0.99:')
print(num_sales_needed_099)
# the proportion of 'weekly' visitors who would need to make a purchase in order to meet that goal
p_sales_needed_099 = num_sales_needed_099/num_visits
print('Proprtion of weekly site visitors need to reach $1,000 revenue at price point $0.99')
print(p_sales_needed_099)

# for price point $1.99
num_sales_needed_199 = 1000/1.99
print('Number of sales needed to reach $1,000 revenue at price point $1.99:')
print(num_sales_needed_199)
p_sales_needed_199 = num_sales_needed_199/num_visits
print('Proprtion of weekly site visitors need to reach $1,000 revenue at price point $1.99')
print(p_sales_needed_199)

# for price point $4.99
num_sales_needed_499 = 1000/4.99
print('Number of sales needed to reach $1,000 revenue at price point $4.99:')
print(num_sales_needed_499)
p_sales_needed_499 = num_sales_needed_499/num_visits
print('Proprtion of weekly site visitors need to reach $1,000 revenue at price point $4.99')
print(p_sales_needed_499)


# to check if the percent of group A (the $0.99 price point) that purchased an upgrade package
# is significantly 'greater' than p_sales_needed_099
# (the percent of visitors who need to buy an upgrade package at $0.99 in order to make our minimum revenue target of $1,000)
# binomial test

# the numbers of group A visitors, the number of group A visitors who made a purchase
samp_size_099 = np.sum(abdata.group == 'A')
print('Number of site visitors in group A:')
print(samp_size_099)
sales_099 = np.sum((abdata.group == 'A') & (abdata.is_purchase == 'Yes'))
print('Number of site visitors in group A who made a purchase:')
print(sales_099)

# the numbers of group B visitors (the $1.99 price point), the number of group B visitors who made a purchase
samp_size_199 = np.sum(abdata.group == 'B')
print('Number of site visitors in group B:')
print(samp_size_199)
sales_199 = np.sum((abdata.group == 'B') & (abdata.is_purchase == 'Yes'))
print('Number of site visitors in group B who made a purchase:')
print(sales_199)

# the numbers of group C visitors (the $4.99 price point), the number of group C visitors who made a purchase
samp_size_499 = np.sum(abdata.group == 'C')
print('Number of site visitors in group C:')
print(samp_size_499)
sales_499 = np.sum((abdata.group == 'C') & (abdata.is_purchase == 'Yes'))
print('Number of site visitors in group C who made a purchase:')
print(sales_499)

# for group A
pvalueA = stat.binom_test(sales_099, samp_size_099, p_sales_needed_099, alternative= 'greater')
print('p-value of group A:')
print(pvalueA)

# for group B
pvalueB = stat.binom_test(sales_199, samp_size_199, p_sales_needed_199, alternative= 'greater')
print('p-value of group B:')
print(pvalueB)

# for group C
pvalueC = stat.binom_test(sales_499, samp_size_499, p_sales_needed_499, alternative= 'greater')
print('p-value of group C:')
print(pvalueC)


# determine which group (A, B or C) had significantly higher purchase rate than $1,000 target
# and how much should product manager charge for the upgrade package based on binomial test p-values
p_values = [pvalueA, pvalueB, pvalueC]
sig_p_value = []

for p_value in p_values:
  if p_value < sig_threshold:
    sig_p_value.append(p_value)
    for p in sig_p_value:
      if p == pvalueA:
        print('The purchase rate of group A is significantly higher than $1,000 target')
        print('Product Manager should charge $0.99 for the upgrade package')
      if p == pvalueB:
        print('The purchase rate of group B is significantly higher than $1,000 target')
        print('Product Manager should charge $1.99 for the upgrade package')
      else:
        print('The purchase rate of group C is significantly higher than $1,000 target')
        print('Product Manager should charge $4.99 for the upgrade package')
      
