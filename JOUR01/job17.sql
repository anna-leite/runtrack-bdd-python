-- Requête pour modifier l'âge de Betty de 23 à 20 ans et afficher ces information mises à jour

uPDATE etudiant SET age = 20 WHERE nom = 'Spaguetti';

SELECT nom, prenom, age FROM etudiant WHERE nom = 'Spaguetti';