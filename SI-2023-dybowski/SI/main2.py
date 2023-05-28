import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from sklearn.linear_model import LinearRegression

# Zestaw danych
years = np.array([[2000], [2002], [2005], [2007], [2010]])
percentages = np.array([6.5, 7.0, 7.4, 8.2, 9.0])

# Inicjalizacja wykresu
fig, ax = plt.subplots()
ax.scatter(years, percentages)

# Tworzenie modelu regresji liniowej
regression_model = LinearRegression()

# Funkcja animacji
def animate(i):
    # Trenowanie modelu z danymi z roku 2000 do roku i
    regression_model.fit(years[:i+1], percentages[:i+1])
    # Wyświetlenie wykresu z dopasowaną linią
    ax.plot(years, regression_model.predict(years), 'r--')
    ax.set_title(f'Przewidywany procent bezrobotnych w 2013: {round(regression_model.predict([[2013]])[0], 3)}')

# Uruchomienie animacji
ani = FuncAnimation(fig, animate, frames=len(years), interval=1000, repeat=False)

# Wyświetlenie animacji
plt.show()
