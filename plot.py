import numpy as np
import matplotlib.pyplot as plt

l = np.arange(0, 5)

plt.plot(l, 'r', label="f(x)=x")

plt.plot(l**2, 'g', label="g(x)=x²")

plt.plot(l**3, 'b', label="h(x)=x³")

plt.legend()

plt.title("Weekly Task 8 Plot")

plt.xlabel("Value of x")

plt.ylabel("Function Solution")

plt.show()