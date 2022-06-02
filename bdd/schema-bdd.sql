DROP DATABASE IF EXISTS qcm_app;
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
INSERT INTO `questions` VALUES (1, "Isaac Newton was","an english scientist,americain politician,jazz musician","an english scientist");
INSERT INTO `questions` VALUES (2, "What happend on June 6, 1944?","World War 2 armistice,Landing in Normandy,liberation of Paris","Landing in Normandy");
INSERT INTO `questions` VALUES (3, "What disability did Ludwig van Beethoven suffer from?","Deafness,Blindness,Dementia","Deafness");
INSERT INTO `questions` VALUES (4, "Which composer did not appear in the movie Amadeus?","Mozart,Salieri,Praetorius","Praetorius");

USE qcm_app;
INSERT INTO `qcm` VALUES (1, "History");
INSERT INTO `qcm` VALUES (2, "Music");

USE qcm_app;
INSERT INTO `join_user_qcm`
VALUES (
  (SELECT id 
  FROM users 
  WHERE pseudo = "user1"),
  (SELECT id 
  FROM qcm 
  WHERE name = "Music")
);

USE qcm_app;
INSERT INTO `join_qcm_questions` 
VALUES (
  (SELECT id 
  FROM questions
  WHERE name ="Isaac Newton was"),
  (SELECT id 
  FROM qcm 
  WHERE name = "History")
);

INSERT INTO `join_qcm_questions`
VALUES (
  (SELECT id 
  FROM questions
  WHERE name ="What happend on June 6, 1944?"),
  (SELECT id 
  FROM qcm 
  WHERE name = "History")
);

INSERT INTO `join_qcm_questions`
VALUES (
  (SELECT id 
  FROM questions
  WHERE name ="What disability did Ludwig van Beethoven suffer from?"),
  (SELECT id 
  FROM qcm 
  WHERE name = "Music")
);

INSERT INTO `join_qcm_questions`
VALUES (
  (SELECT id 
  FROM questions
  WHERE name ="Which composer did not appear in the movie Amadeus?"),
  (SELECT id 
  FROM qcm 
  WHERE name = "Music")
);
