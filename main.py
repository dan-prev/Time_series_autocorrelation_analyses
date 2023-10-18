import pandas as pd
import numpy as np
from pandas_datareader import data
from statsmodels.graphics.tsaplots import plot_acf
import matplotlib.pyplot as plt
from statsmodels.stats.diagnostic import acorr_ljungbox

#PART 1 - Time series analysis of differentiated global labor force participation rate

# Retrieving the data and plotting the sample autocorrelation functions
start_date = "2000-01-01"
end_date = "2022-12-31"
series_code = "CIVPART"
df = data.DataReader(series_code, data_source="fred", start=start_date, end=end_date)
# Differentiate the data
differentiated_data = df[series_code].diff()
# Plot ACF for the differentiated data
fig, ax = plt.subplots(figsize=(10,6))
plot_acf(differentiated_data.dropna(), lags=50, ax=ax)
plt.xlabel('Lag')
plt.ylabel('Autocorrelation')
plt.title('Sample Autocorrelation Function (ACF) for Differentiated Labor Force Participation Rate')
plt.show()

#Testing whether p1 is zero, using a 95% confidence level
correlations = differentiated_data.autocorr(lag=1)
n = len(differentiated_data.dropna())
conf_level = 1.96 / np.sqrt(n)
print(f"Autocorrelation at lag 1 for differentiated_data: {correlations:.5f}")
print(f"95% Confidence Interval: ±{conf_level:.5f}")
if abs(correlations) > conf_level:
 print("Conclusion: ρ1 for differentiated_data is statistically different from zero at the 95% confidence level.")
else:
 print("Conclusion: ρ1 for differentiated_data is not statistically different from zero at the 95% confidence level.")

# Performing the Ljung-Box test
lags = 20
results = acorr_ljungbox(differentiated_data.dropna(), lags=lags)
test_statistics = results.lb_stat
p_values = results.lb_pvalue
print("\nLjung-Box Test for differentiated_data:")
print("Lag Test Statistic p-value")
print("-" * 37)
for lag, test_stat, p_val in zip(range(1, lags + 1), test_statistics, p_values):
 print(f"{lag:3d} {test_stat:16.3f} {p_val:10.6f}")
# Interpretation based on p-values:
significance_level = 0.05
if any(p < significance_level for p in p_values):
 print("\nAt least one of the p-values is below 0.05, suggesting the residuals might not be independently distributed.")
else:
 print("\nAll p-values are above 0.05, suggesting the residuals might be independently distributed.")

#PART 2 - Time series analysis for crude birth rate in the United Kingdom

# Retrieving the data and plotting the sample autocorrelation functions
start_date = "2000-01-01"
end_date = "2022-12-31"
series_code = "SPDYNCBRTINGBR"
df = data.DataReader(series_code, data_source="fred", start=start_date, end=end_date)
# Differentiate the data
differentiated_data = df[series_code].diff()
# Plot ACF for the differentiated data
fig, ax = plt.subplots(figsize=(10,6))
plot_acf(differentiated_data.dropna(), lags=20, ax=ax)
plt.xlabel('Lag')
plt.ylabel('Autocorrelation')
plt.title('Sample Autocorrelation Function (ACF) for crude birth rate in the United Kingdom')
plt.show()

#Testing whether p1 is zero, using a 95% confidence level
correlations = differentiated_data.autocorr(lag=1)
n = len(differentiated_data.dropna())
conf_level = 1.96 / np.sqrt(n)
print(f"Autocorrelation at lag 1 for differentiated_data: {correlations:.5f}")
print(f"95% Confidence Interval: ±{conf_level:.5f}")
if abs(correlations) > conf_level:
 print("Conclusion: ρ1 for differentiated_data is statistically different from zero at the 95% confidence level.")
else:
 print("Conclusion: ρ1 for differentiated_data is not statistically different from zero at the 95% confidence level.")

# Performing the Ljung-Box test
lags = 20
results = acorr_ljungbox(differentiated_data.dropna(), lags=lags)
test_statistics = results.lb_stat
p_values = results.lb_pvalue
print("\nLjung-Box Test for differentiated_data:")
print("Lag Test Statistic p-value")
print("-" * 37)
for lag, test_stat, p_val in zip(range(1, lags + 1), test_statistics, p_values):
 print(f"{lag:3d} {test_stat:16.3f} {p_val:10.6f}")
# Interpretation based on p-values:
significance_level = 0.05
if any(p < significance_level for p in p_values):
 print("\nAt least one of the p-values is below 0.05, suggesting the residuals might not be independently distributed.")
else:
 print("\nAll p-values are above 0.05, suggesting the residuals might beindependently distributed.")

#PART 3 - Time series analysis for global Producer Price Index (PPI) by industry for deep sea freight

# Retrieving the data and plotting the sample autocorrelation functions
start_date = "2000-01-01"
end_date = "2022-12-31"
series_code = "SPDYNCBRTINGBR"
df = data.DataReader(series_code, data_source="fred", start=start_date, end=end_date)
# Differentiate the data
differentiated_data = df[series_code].diff()
# Plot ACF for the differentiated data
fig, ax = plt.subplots(figsize=(10,6))
plot_acf(differentiated_data.dropna(), lags=20, ax=ax)
plt.xlabel('Lag')
plt.ylabel('Autocorrelation')
plt.title('Sample Autocorrelation Function (ACF) for crude birth rate in the United Kingdom')
plt.show()

#Testing whether p1 is zero, using a 95% confidence level
correlations = differentiated_data.autocorr(lag=1)
n = len(differentiated_data.dropna())
conf_level = 1.96 / np.sqrt(n)
print(f"Autocorrelation at lag 1 for differentiated_data: {correlations:.5f}")
print(f"95% Confidence Interval: ±{conf_level:.5f}")
if abs(correlations) > conf_level:
 print("Conclusion: ρ1 for differentiated_data is statistically different from zero at the 95% confidence level.")
else:
 print("Conclusion: ρ1 for differentiated_data is not statistically different from zero at the 95% confidence level.")

# Performing the Ljung-Box test
lags = 20
results = acorr_ljungbox(differentiated_data.dropna(), lags=lags)
test_statistics = results.lb_stat
p_values = results.lb_pvalue
print("\nLjung-Box Test for differentiated_data:")
print("Lag Test Statistic p-value")
print("-" * 37)
for lag, test_stat, p_val in zip(range(1, lags + 1), test_statistics, p_values):
 print(f"{lag:3d} {test_stat:16.3f} {p_val:10.6f}")
# Interpretation based on p-values:
significance_level = 0.05
if any(p < significance_level for p in p_values):
 print("\nAt least one of the p-values is below 0.05, suggesting the residuals might not be independently distributed.")
else:
 print("\nAll p-values are above 0.05, suggesting the residuals might be indipendently distributed.")