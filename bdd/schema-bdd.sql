CREATE DATABASE if not exists qcm_app;

USE qcm_app;

CREATE TABLE `users` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `pseudo` varchar(255),
  `password` varchar(255),
  `created_at` timestamp
);

CREATE TABLE `join_user_qcm` (
  `user_id` int,
  `qcm_id` int
);

CREATE TABLE `qcm` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255)
);

CREATE TABLE `join_qcm_questions` (
  `question_id` int,
  `qcm_id` int
);

CREATE TABLE `questions` (
  `id` int PRIMARY KEY AUTO_INCREMENT,
  `name` varchar(255),
  `answers` varchar(255),
  `correct_answer` varchar(255)
);

ALTER TABLE `join_user_qcm` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `join_user_qcm` ADD FOREIGN KEY (`qcm_id`) REFERENCES `qcm` (`id`);

ALTER TABLE `join_qcm_questions` ADD FOREIGN KEY (`qcm_id`) REFERENCES `qcm` (`id`);

ALTER TABLE `join_qcm_questions` ADD FOREIGN KEY (`question_id`) REFERENCES `questions` (`id`);
