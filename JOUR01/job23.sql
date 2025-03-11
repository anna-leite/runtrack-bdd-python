-- Requête pour récupérer les information de l'étudiant le plus agé

SELECT * FROM etudiant ORDER BY age DESC LIMIT 1;

-- Autre solution :
-- SELECT * FROM etudiant WHERE age = (SELECT MAX(age) FROM etudiant); 