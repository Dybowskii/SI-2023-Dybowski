import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Zestaw danych
years = np.array([[2000], [2002], [2005], [2007], [2010]])
percentages = np.array([6.5, 7.0, 7.4, 8.2, 9.0])

# Tworzenie modelu regresji liniowej
regression_model = LinearRegression()

# Trenowanie modelu
regression_model.fit(years, percentages)

# Wyświetlenie współczynników
print("Współczynnik nachylenia: ", regression_model.coef_[0])
print("Punkt przecięcia: ", regression_model.intercept_)

# Przewidywanie procentu bezrobotnych w roku 2013

year = 2010
predicted_percentage = regression_model.predict([[year]])

while round(predicted_percentage[0], 3) < 12:
    predicted_percentage = regression_model.predict([[year]])
    print(f"Przewidywany procent bezrobotnych w {year}: ", round(predicted_percentage[0], 3))
    year = year + 1
