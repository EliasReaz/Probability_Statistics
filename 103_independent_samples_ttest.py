# import packages
from scipy.stats import ttest_ind, norm
import matplotlib.pyplot as plt 
import numpy as np

## generate population
sample_a = norm.rvs(loc=500, scale=100, size=200, random_state=42).astype(int)
sample_b = norm.rvs(loc=550, scale=150, size=100, random_state=42).astype(int)
# print(len(population))
#plt.hist(population)

np.random.seed(42)
sample_a_mean = sample_a.mean()
sample_b_mean = sample_b.mean()

print(f"Mean of sample A: {sample_a_mean}")
print(f"Mean of sample B: {sample_b_mean}")

## State Null and Alternate Hypothesis
null_hypothesis = "The mean of the sample A is equal to the mean of sample B"
alternate_hypothesis = "The mean of sample A is different to the mean of sample B"
acceptance_criteria = 0.05


t_statistic, p_val = ttest_ind(sample_a, sample_b)

print(f"t statistic: {round(t_statistic,2)} and p_val {round(p_val,2)}")

## Print the result (p-val)
if p_val <= acceptance_criteria:
    print(f"As p-val {round(p_val,4)} is lower than acceptance_criteria of {acceptance_criteria}, we reject the null_hypothesis and conclude that {alternate_hypothesis}")
else:
    print(f"As p-val {round(p_val,4)} is higher than acceptance_criteria of {acceptance_criteria}, we retain the null_hypothesis: {null_hypothesis}")

## WELCH'S t-test
## ttest_ind assumes that two sample has equal variance, 
## so we use Welch's ttest because sample variance are not equal
t_statistic, p_val = ttest_ind(sample_a, sample_b, equal_var=False)

print(f"Welch's t statistic: {round(t_statistic,2)} and p_val {round(p_val,2)}")

## Print the result (p-val)
if p_val <= acceptance_criteria:
    print(f"As p-val {round(p_val,4)} is lower than acceptance_criteria of {acceptance_criteria}, we reject the null_hypothesis and conclude that {alternate_hypothesis}")
else:
    print(f"As p-val {round(p_val,4)} is higher than acceptance_criteria of {acceptance_criteria}, we retain the null_hypothesis: {null_hypothesis}")

