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
monthly.head()

# IT HAS NOT COMPLETED YET
