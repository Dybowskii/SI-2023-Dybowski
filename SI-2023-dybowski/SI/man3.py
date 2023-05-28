import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from sklearn.linear_model import LinearRegression

years = np.array([[2000], [2002], [2005], [2007], [2010]])
percentages = np.array([6.5, 7.0, 7.4, 8.2, 9.0])

fig, ax = plt.subplots()
ax.scatter(years, percentages)

regression_model = LinearRegression()

line, = ax.plot([], [], 'r--')
def animate(i):
    regression_model.fit(years[:i+1], percentages[:i+1])
    line.set_data(years, regression_model.predict(years))

ani = FuncAnimation(fig, animate, frames=len(years), interval=1000, repeat=False)

plt.show()
