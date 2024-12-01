import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

df = pd.read_csv("epa-sea-level.csv") # Reading the CSV file and storing it in a dataframe.

df.dropna(subset=["Year","CSIRO Adjusted Sea Level"], inplace=True) # Removing any NAN value holding coloums or rows.

x = df["Year"]
y = df["CSIRO Adjusted Sea Level"]

slope, intercept, r_value, p_value, std_err = linregress(x, y) # Finding the SLOPE, INTERCEPT of the given Panda series.

x_extend = np.arange(1881, 2051) # Extending the x axis to get the prediction.
y_extend = slope * x_extend + intercept # Extending the y axis in respect of the already extedended x axis, so we dont get any Valuerrorr about dimensions.

plt.scatter(x, y, c="blue") # Im using Scatter plot, you can use anyone, but scatterplot is preferred for these type of data.
plt.plot(x_extend, y_extend, c="red", label="Best fit line") # Plotting the line to actually predict the value of the Sealevel in the upcoming year.
plt.xlabel("Year") 
plt.ylabel("Sea Level(Inches)")
plt.title("Rise in Sea Level")
plt.show() # Output.

