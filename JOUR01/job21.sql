-- Requête pour compter le nombre d'étudiants dont l'âge est compris entre 18 et 25 ans présents en base de données

SELECT COUNT(*) FROM etudiant WHERE age BETWEEN 18 AND 25;

-- SELECT COUNT(*) FROM etudiant WHERE age > 18 AND age < 25;