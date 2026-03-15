Skrypt ekstrahujący dane do modelu optymalizacji zużycia prądu 5G
-- Wynik tego zapytania eksportujemy do pliku: dane_5g.csv

SELECT
    n.liczba_aktywnych_uzytkownikow AS Uzytkownicy,
    p.zuzycie_pradu_kwh AS Zuzycie_Pradu
FROM
    nadajniki_5g n
JOIN
    pomiary_energetyczne p ON n.id_nadajnika = p.id_nadajnika
WHERE
    n.status_urzadzenia = 'Aktywny'
    AND p.data_pomiaru >= '2026-03-01' -- Bierzemy tylko świeże dane z tego miesiąca
ORDER BY
    n.liczba_aktywnych_uzytkownikow ASC;
