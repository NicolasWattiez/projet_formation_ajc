DROP DATABASE qcm_app;
CREATE DATABASE if not exists qcm_app;

USE qcm_app;

CREATE TABLE if not exists `users` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `pseudo` varchar(255),
  `password` varchar(255),
  `role` varchar(255),
  `created_at` timestamp
);

CREATE TABLE if not exists `join_user_qcm` (
  `user_id` int,
  `qcm_id` int
);

CREATE TABLE if not exists `qcm` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255)
);

CREATE TABLE if not exists `join_qcm_questions` (
  `question_id` int,
  `qcm_id` int
);

CREATE TABLE if not exists `questions` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255),
  `answers` varchar(255),
  `correct_answer` varchar(255)
);

ALTER TABLE `join_user_qcm` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `join_user_qcm` ADD FOREIGN KEY (`qcm_id`) REFERENCES `qcm` (`id`);

ALTER TABLE `join_qcm_questions` ADD FOREIGN KEY (`qcm_id`) REFERENCES `qcm` (`id`);

ALTER TABLE `join_qcm_questions` ADD FOREIGN KEY (`question_id`) REFERENCES `questions` (`id`);

INSERT INTO `users` VALUES (1, "admin" ,"admin","admin", NOW());
INSERT INTO `users` VALUES (2, "user1" ,"password1","member", NOW());
INSERT INTO `users` VALUES (3, "user2" ,"password","member", NOW());

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
