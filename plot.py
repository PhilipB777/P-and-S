# Philip Brady
# This is the Weekly Task 8.
# The program displays a plot of the functions
# f(x)=x, g(x)=x² and h(x)=x³ in the range 0-4
# on the one set of axes.

# The numpy module is imported.
import numpy as np
# The pyplot module is imported from the
# matplotlib library.
import matplotlib.pyplot as plt

# A range of values from 0 to 4. The increments
# of 0.1 improve the plots visually.
x = np.arange(0.0, 4.1, 0.1)

# Plot for x in red dots.
plt.plot(x, x, 'r.', label="f(x)=x")
# Plot for x² in green dots.
plt.plot(x, x**2, 'g.', label="g(x)=x²")
# Plot for x³ in blue dots.
plt.plot(x, x**3, 'b.', label="h(x)=x³")
# Labels displayed.
plt.legend()
# Useful headings for explanation.
plt.title("Plot of Functions")
plt.xlabel("Value of x")
plt.ylabel("Function of x")
# Scatterplot displayed to user.
plt.show()

# Reference:
# https://realpython.com/python-matplotlib-guide/