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
