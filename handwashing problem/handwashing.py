import pandas as pd

# reading csv file using pandas library
yearly = pd.read_csv("datasets/yearly_deaths_by_clinic.csv")

yearly["proportion_deaths"] = yearly["deaths"] / yearly["births"]
yearly1 = yearly[yearly["clinic"] == 'clinic 1']
yearly2 = yearly[yearly["clinic"] == 'clinic 2']

# IT HAS NOT COMPLETED YET
