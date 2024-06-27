# import packages
from scipy.stats import ttest_1samp, norm
import matplotlib.pyplot as plt 
import numpy as np

## generate population
population = norm.rvs(loc=500, scale=100, size=1000, random_state=42).astype(int)

print(len(population))
#plt.hist(population)

np.random.seed(42)
sample = np.random.choice(population, size=250)

pop_mean = np.mean(population)
sample_mean = np.mean(sample)

print(f"Population mean: {pop_mean}")
print(f"sample mean: {sample_mean}")

## State Null and Alternate Hypothesis
null_hypothesis = "The mean of the sample is equal to the mean of the population"
alternate_hypothesis = "the mean of the sample is different to the mean of the population"
acceptance_criteria = 0.05


t_statistic, p_val = ttest_1samp(sample, popmean=pop_mean)

print(f"t statistic: {round(t_statistic,2)} and p_val {round(p_val,2)}")

## Print the result (p-val)
if p_val <= acceptance_criteria:
    print(f"As p-val {round(p_val,4)} is lower than acceptance_criteria of {acceptance_criteria}, we reject the null_hypothesis and conclude that {alternate_hypothesis}")
else:
    print(f"As p-val {round(p_val,4)} is higher than acceptance_criteria of {acceptance_criteria}, we retain the null_hypothesis: {null_hypothesis}")



