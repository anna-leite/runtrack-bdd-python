-- Requête pour calculer la moyenne d'âge des étudiants

SELECT SUM(age) / COUNT(age) AS moyenne_age FROM etudiant;

-- Autres solutions :
-- SELECT AVG(age) AS moyenne_age FROM etudiant WHERE age IS NOT NULL;

-- SELECT (SELECT SUM(age) FROM etudiant) / (SELECT COUNT(age) FROM etudiant) AS moyenne_age;