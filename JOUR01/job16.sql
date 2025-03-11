-- Requête pour trier les élèves dont le prénom commence par un "b"

 SELECT * FROM etudiant WHERE LOWER(nom) LIKE 'b%';
