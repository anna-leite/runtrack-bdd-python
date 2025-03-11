-- Requête pour récupérer les élèves dont l'âge est compris entre 16 et 25 ans 

SELECT * FROM etudiant WHERE age > 16 AND age < 25;

-- solution qui inclue l'élève agé de 16 ans :
--  SELECT * FROM etudiant WHERE age BETWEEN 16 AND 25;
