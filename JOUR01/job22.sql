-- Requête pour récupérer les information de l'étudiant le plus jeune 

SELECT * FROM etudiant ORDER BY age ASC LIMIT 1;

-- Autre solution :
-- SELECT * FROM etudiant WHERE age = (SELECT MIN(age) FROM etudiant);
