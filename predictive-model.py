import sympy as 
import pandas as pd

# 1. Definicja zmiennych symbolicznych dla modelu matematycznego
x, y, a, b = sp.symbols("x y a b")

# Równanie regresji liniowej i funkcja straty (Błąd Średniokwadratowy - MSE)
line_eq = a * x + b
loss = (y - line_eq) ** 2

# 2. Wyliczenie pochodnych cząstkowych (gradientów) za pomocą SymPy
grad_a_expr = sp.diff(loss, a)
grad_b_expr = sp.diff(loss, b)

# Zamiana wyrażeń symbolicznych na funkcje Pythona
calculate_grad_a = sp.lambdify((x, y, a, b), grad_a_expr)
calculate_grad_b = sp.lambdify((x, y, a, b), grad_b_expr)

# 3. Wczytanie danych o zużyciu energii w sieci 5G
df = pd.read_csv("dane_5g.csv")
x_data = df['uzytkownicy'].tolist()
y_data = df['zuzycie_pradu'].tolist()

# 4. Inicjalizacja hiperparametrów modelu (Stochastic Gradient Descent)
learning_rate = 0.000001
epochs = 10000
a_current = 0.0
b_current = 0.0

print("Rozpoczęcie trenowania modelu AI...")

# 5. Pętla ucząca model 
for epoch in range(epochs):
    for i in range(len(x_data)):
        x_val = x_data[i]
        y_val = y_data[i]

        # Obliczenie gradientu dla obecnej próbki
        grad_a = calculate_grad_a(x_val, y_val, a_current, b_current)
        grad_b = calculate_grad_b(x_val, y_val, a_current, b_current)

        # Aktualizacja wag modelu (krok w dół gradientu)
        a_current = a_current - (learning_rate * grad_a)
        b_current = b_current - (learning_rate * grad_b)

print("Trenowanie zakończone z sukcesem!")
print(f"Wyliczony parametr 'a' (wspływ użytkowników na prąd): {a_current:.4f}")
print(f"Wyliczony parametr 'b' (bazowe zużycie prądu): {b_current:.4f}")
