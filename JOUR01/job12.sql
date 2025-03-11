-- Requête pour récupérer les membres d'une même famille

SELECT * FROM etudiant 
WHERE nom IN (
    SELECT nom FROM etudiant
    GROUP BY nom
    HAVING COUNT(*) > 1
);
