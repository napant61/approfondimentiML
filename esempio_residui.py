from sklearn.datasets import fetch_california_housing
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# Carica i dati California Housing
data = fetch_california_housing()
X = pd.DataFrame(data.data, columns=data.feature_names)
y = data.target

# Mostra qualche riga
print(X.head())


# Usiamo solo una feature per semplicità
X = X[['MedInc']]

# Divisione train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Costruzione modello
model = LinearRegression()
model.fit(X_train, y_train)

# Predizione
y_pred = model.predict(X_test)

residuals = y_test - y_pred
# Scatter plot dei residui
plt.figure(figsize=(8,5))
plt.scatter(y_pred, residuals, alpha=0.5)
plt.axhline(y=0, color='red', linestyle='--')
plt.xlabel('Predicted Values')
plt.ylabel('Residuals')
plt.title('Residual Plot')
plt.show()

from sklearn.ensemble import RandomForestRegressor

# Modello Random Forest
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)

# Alleniamo sul dataset originale (MedInc come feature)
rf_model.fit(X_train, y_train)

# Predizione
y_pred_rf = rf_model.predict(X_test)

# Calcolo dei residui
residuals_rf = y_test - y_pred_rf

plt.figure(figsize=(8,5))
plt.scatter(y_pred_rf, residuals_rf, alpha=0.5, color='purple')
plt.axhline(y=0, color='red', linestyle='--')
plt.xlabel('Predicted Values (Random Forest)')
plt.ylabel('Residuals')
plt.title('Residual Plot - Random Forest')
plt.show()

print("R2 Random Forest:", rf_model.score(X_test, y_test))