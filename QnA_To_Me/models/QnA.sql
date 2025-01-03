CREATE TABLE User (
  id INT NOT NULL AUTO_INCREMENT,
  name VARCHAR(50) NOT NULL,
  email VARCHAR(100) NOT NULL,
  join_date DATETIME NOT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE Question (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    contents VARCHAR(255) NOT NULL,
    category VARCHAR(50) NOT NULL,
    create_date DATETIME NOT NULL
);

CREATE TABLE Answer (
    id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    answer_contents VARCHAR(255) NOT NULL,
    answer_date DATETIME NOT NULL,
    user_id INT,
    question_id INT,
    FOREIGN KEY (user_id) REFERENCES user(id),
    FOREIGN KEY (question_id) REFERENCES question(id)
);


INSERT INTO User (name, email, join_date)
VALUES ('원설아', 'seolalny@gmail.com', '2024-03-25 14:00:00');

INSERT INTO Question (contents, category, create_date)
VALUES ('내가 가장 좋아하는 음식은?', 'Meal', '2024-03-25 14:00:00');

INSERT INTO answer (answer_contents, answer_date, user_id, question_id)
VALUES ('삼겹살 구이', '2024-03-25 14:01:00', 1, 1);


SELECT Answer.user_id, Question.id, Answer.id, Question.contents, Answer.answer_contents
FROM Answer
INNER JOIN Question ON Answer.question_id = Question.id;
