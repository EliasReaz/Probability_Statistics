## import packages

import pandas as pd
from scipy.stats import chi2_contingency, chi2

## load campaign data
campaign_data = pd.read_excel("grocery_database.xlsx", sheet_name="campaign_data")

print(campaign_data.head(2))
print("rows and cols: ", campaign_data.shape)

## drop rows with "Control" group
campaign_data = campaign_data.loc[campaign_data["mailer_type"] != "Control"]

print(campaign_data.shape)

## State Null and Alternate Hypothesis
null_hypothesis = "There is no relationship between mailer_type and signup. They are indepedent."
alternate_hypothesis = "There is a relationship between mailer_type and signup. They are not indepedent."
acceptance_criteria = 0.05
## Get expected observations and chi2 statistics
observed_data = pd.crosstab(campaign_data["mailer_type"], campaign_data["signup_flag"])

# print(observed_data)

observed_data = observed_data.values

print(observed_data)


chi2_statistic, p_val, dof, expected_obs = chi2_contingency(observed_data)

print(f"chi2_statistics: {round(chi2_statistic,4)} and p-val: {round(p_val,4)}")

## Get critical statistic for our test
critical_statistic = chi2.ppf(1 - acceptance_criteria, dof)

print(f"critical statistic: {critical_statistic}")

## Print the result (p-val)
if p_val <= acceptance_criteria:
    print(f"As p-val {round(p_val,4)} is lower than acceptance_criteria of {acceptance_criteria}, we reject the null_hypothesis and conclude that {alternate_hypothesis}")
else:
    print(f"As p-val {round(p_val,4)} is higher than acceptance_criteria of {acceptance_criteria}, we retain the null_hypothesis: {null_hypothesis}")
      
# print the result, chi2_statistic
      
if chi2_statistic >= critical_statistic:
    print(f"As chi2 statistic {round(chi2_statistic,4)} is higher than critical statistic of {round(critical_statistic,4)}, we reject the null_hypothesis: {null_hypothesis}")
else:
    print(f"As chi2 statistic {round(chi2_statistic,4)} is lower than critical statistic of {round(critical_statistic,4)},, we retain the null_hypothesis: {null_hypothesis}")
