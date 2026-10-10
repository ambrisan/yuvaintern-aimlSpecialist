import statistics
import math

# Sample dataset representing hours spent on a project
hours = [12, 15, 15, 18, 22, 25, 30]

# Descriptive Statistics
mean_val = statistics.mean(hours)
median_val = statistics.median(hours)
mode_val = statistics.mode(hours)
variance_val = statistics.variance(hours)
std_dev = statistics.stdev(hours)

print("\n--- Descriptive Statistics ---")
print(f"Dataset: {hours}")
print(f"Mean: {mean_val:.2f}")
print(f"Median: {median_val}")
print(f"Mode: {mode_val}")
print(f"Variance: {variance_val:.2f}")
print(f"Standard Deviation: {std_dev:.2f}")

# Percentiles (using manual calculation for 75th percentile)
hours.sort()
index_75th = math.ceil(0.75 * len(hours)) - 1
print(f"75th Percentile: {hours[index_75th]}")

# Basic Correlation (Pearson's r) between hours and theoretical scores
scores_y = [60, 70, 75, 80, 85, 90, 95]
mean_y = statistics.mean(scores_y)

# Calculating covariance and standard deviations for correlation
covariance = sum((x - mean_val) * (y - mean_y) for x, y in zip(hours, scores_y)) / (len(hours) - 1)
std_dev_y = statistics.stdev(scores_y)
correlation = covariance / (std_dev * std_dev_y)

print(f"\nCorrelation between Hours and Scores: {correlation:.2f}")