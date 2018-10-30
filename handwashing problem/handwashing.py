import pandas as pd
import matplotlib.pyplot as plt

# reading csv file using pandas library
yearly = pd.read_csv("datasets/yearly_deaths_by_clinic.csv")

yearly["proportion_deaths"] = yearly["deaths"] / yearly["births"]
yearly1 = yearly[yearly["clinic"] == 'clinic 1']
yearly2 = yearly[yearly["clinic"] == 'clinic 2']

# Plotting the yearly proportion of deaths for both clinics.
ax = yearly1.plot('year', 'proportion_deaths', label='Clinic 1')
yearly2.plot('year', 'proportion_deaths', label='Clinic 1', ax = ax)
ax.legend(loc = 0)
ax.set_ylabel('Proportion Deaths')

# Reading datasets/monthly_deaths.csv into monthly
monthly = pd.read_csv('datasets/monthly_deaths.csv', parse_dates=['date'])

# Calculating proportion of deaths per no. births
monthly["proportion_deaths"] = monthly["deaths"] / monthly["births"]

# Printing out the first rows in monthly
monthly.head(5)

# Plotting monthly proportion of deaths
ax = monthly.plot('date', 'proportion_deaths')
ax.set_ylabel('Proportion Deaths')


# Date when handwashing was made mandatory
handwashing_start = pd.to_datetime('1847-06-01')

# Splitting monthly into before and after handwashing_start
before_washing = monthly[monthly["date"] < handwashing_start]
after_washing = monthly[monthly["date"] >= handwashing_start]

# Plotting monthly proportion of deaths before and after handwashing
ax = before_washing.plot("date", "proportion_deaths", label='Before Washing', color='b')
after_washing.plot("date", "proportion_deaths", label="After Washing", ax = ax, color='r')
ax.set_ylabel('Proportion Deaths')

# Difference in mean monthly proportion of deaths due to handwashing
before_proportion = before_washing["proportion_deaths"]
after_proportion = after_washing["proportion_deaths"]
mean_diff = after_proportion.mean() - before_proportion.mean()
print(mean_diff)
# IT HAS NOT COMPLETED YET
