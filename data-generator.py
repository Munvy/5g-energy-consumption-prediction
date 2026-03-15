import pandas as 
import random

# Listy do przechowywania wygenerowanych danych
users_list = []
power_list = []

print("Rozpoczęcie generowania syntetycznych danych dla nadajników 5G...")

# Generowanie 1000 realistycznych próbek
for x in range(1000):
    # Losowa liczba aktywnych użytkowników (od 1 do 1000)
    users = random.randint(1, 1001)
    
    # Dodanie naturalnego "szumu" (wahań sieci)
    noise = random.uniform(-3.0, 3.0)
    
    # Wzór na zużycie prądu (bazowe 12 kWh + 0.07 za każdego użytkownika + szum)
    calculated_power = 12 + (0.07 * users) + noise
    
    users_list.append(users)
    power_list.append(calculated_power)

# Stworzenie tabeli i zapisanie jej do pliku CSV
df = pd.DataFrame({
    'uzytkownicy': users_list,
    'zuzycie_pradu': power_list
})

df.to_csv('dane_5g.csv', index=False)
print("1000 wierszy wygenerowane i zapisane w pliku dane_5g.csv!")
