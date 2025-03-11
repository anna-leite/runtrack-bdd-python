-- Requête pour récupérer les élèves dont l'âge est compris entre 16 et 25 ans en triant par l'âge des étudiants par ordre croissant

SELECT * FROM etudiant WHERE age BETWEEN 16 AND 25 ORDER BY age ASC;