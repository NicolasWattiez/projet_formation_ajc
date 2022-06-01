USE qcm_app;
INSERT INTO `users` VALUES (1, "user1" ,"password1", NOW());
INSERT INTO `users` VALUES (2, "user2" ,"password2", NOW());
INSERT INTO `users` VALUES (3, "user3" ,"password3", NOW());

USE qcm_app;
INSERT INTO `questions` VALUES (1, "Isaac Newton était","savant anglais,homme politique américain,musicien de jazz","savant anglais");
INSERT INTO `questions` VALUES (2, "Que c'est il passé le 6 juin 1944?","Armistice 2nd Guerre Mondiale,Débarquement en Normandie,Libération de Paris","Débarquement en Normandie");
INSERT INTO `questions` VALUES (3, "De quel handicap souffrait Ludwig van Beethoven?","Surdité,Cécité politique américain,Démence","Surdité");
INSERT INTO `questions` VALUES (4, "Quel compositeur n'est pas représenté dans le film Amadeus?","Mozart,Salieri,Praetorius","Praetorius");

USE qcm_app;
INSERT INTO `qcm` VALUES (1, "Histoire");
INSERT INTO `qcm` VALUES (2, "Musique");

USE qcm_app;
INSERT INTO `join_user_qcm`
VALUES (
  (SELECT id 
  FROM users 
  WHERE pseudo = "user1"),
  (SELECT id 
  FROM qcm 
  WHERE name = "Musique")
);

USE qcm_app;
INSERT INTO `join_qcm_questions` 
VALUES (
  (SELECT id 
  FROM questions
  WHERE name ="Isaac Newton était"),
  (SELECT id 
  FROM qcm 
  WHERE name = "Histoire")
);

INSERT INTO `join_qcm_questions`
VALUES (
  (SELECT id 
  FROM questions
  WHERE name ="Que c'est il passé le 6 juin 1944?"),
  (SELECT id 
  FROM qcm 
  WHERE name = "Histoire")
);

INSERT INTO `join_qcm_questions`
VALUES (
  (SELECT id 
  FROM questions
  WHERE name ="De quel handicap souffrait Ludwig van Beethoven?"),
  (SELECT id 
  FROM qcm 
  WHERE name = "Musique")
);

INSERT INTO `join_qcm_questions`
VALUES (
  (SELECT id 
  FROM questions
  WHERE name ="Quel compositeur n'est pas représenté dans le film Amadeus?"),
  (SELECT id 
  FROM qcm 
  WHERE name = "Musique")
);
