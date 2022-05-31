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