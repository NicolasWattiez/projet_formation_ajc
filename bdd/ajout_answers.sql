INSERT INTO `answers`
VALUES ( 1, "A=savant anglais B=homme politique américain C=musicien de jazz","A",
  (SELECT id 
  FROM questions 
  WHERE name = "Isaac Newton était")
);

INSERT INTO `answers`
  VALUES ( 2, "A=Armistice 2nd Guerre Mondiale B=Débarquement en Normandie C=Libération de Paris","B",
  (SELECT id 
  FROM questions 
  WHERE name = "Que c'est il passé le 6 juin 1944")
);

 INSERT INTO `answers`
VALUES ( 3, "A= Surdité B= Cécité politique américain C= Démence","A",
   (SELECT id 
   FROM questions 
   WHERE name = "De quel handicap souffrait Ludwig van Beethoven fut-il atteint au cours de sa vie")
 );

INSERT INTO `answers`
VALUES ( 4, "A= Mozart B= Salieri C= Praetorius","C",
  (SELECT id 
  FROM questions 
  WHERE name = "Quel compositeur n'est pas représenté dans le film Amadeus")
);

