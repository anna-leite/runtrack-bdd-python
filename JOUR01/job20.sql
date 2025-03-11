-- Requête pour compter le nombre d'étuudiants mineurs présents en base de données

SELECT COUNT(*) FROM etudiant WHERE age < 18;