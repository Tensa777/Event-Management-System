Create  database event_mgmt;

use event_mgmt;

CREATE TABLE events (
    event_id INT AUTO_INCREMENT PRIMARY KEY,
    event_title VARCHAR(255),
    event_price INT,
    participants INT,
    type_id INT,
    location_id INT,
    date DATE
);

INSERT INTO events (event_title, event_price, participants, type_id, location_id, date) VALUES
('Tech Fest 2025', 100, 250, 1, 101, '2025-04-20'),
('Cultural Night', 50, 500, 2, 102, '2025-04-25'),
('Coding Hackathon', 0, 150, 1, 101, '2025-05-02'),
('Sports Day', 30, 200, 3, 103, '2025-04-22'),
('Entrepreneurship Talk', 0, 100, 4, 104, '2025-04-18'),
('Photography Workshop', 200, 60, 5, 105, '2025-05-05'),
('Drama Club Performance', 20, 80, 2, 102, '2025-04-28'),
('Science Exhibition', 0, 300, 1, 106, '2025-05-01'),
('Music Battle', 50, 120, 2, 102, '2025-04-30'),
('AI & ML Seminar', 150, 90, 4, 101, '2025-05-10');


CREATE TABLE participants (
    p_id INT AUTO_INCREMENT PRIMARY KEY,
    event_id INT,
    fullname VARCHAR(255),
    email VARCHAR(255),
    mobile VARCHAR(15),
    college VARCHAR(255),
    branch_id INT
);

CREATE TABLE event_type (
    type_id INT AUTO_INCREMENT PRIMARY KEY,
    type_name VARCHAR(255)
);

INSERT INTO event_type (type_name) VALUES
('Technical'),
('Cultural'),
('Sports'),
('Seminar'),
('Workshop'),
('Competition'),
('Social'),
('Awareness Drive');


CREATE TABLE location (
    location_id INT AUTO_INCREMENT PRIMARY KEY,
    location_name VARCHAR(255)
);
INSERT INTO location (location_name) VALUES
('Auditorium - Main Campus'),
('Seminar Hall - Block A'),
('Open Air Theatre'),
('Sports Ground'),
('Innovation Lab'),
('Library Conference Room'),
('Cafeteria Lawn'),
('Computer Science Block'),
('Cultural Centre - Block C'),
('Main Gate Plaza');


CREATE TABLE branch (
    branch_id INT AUTO_INCREMENT PRIMARY KEY,
    branch_name VARCHAR(255)
);

INSERT INTO branch (branch_name) VALUES
('Computer Science and Engineering'),
('Information Science'),
('Electronics and Communication'),
('Mechanical Engineering'),
('Civil Engineering'),
('Electrical and Electronics'),
('Artificial Intelligence and Data Science'),
('Biotechnology'),
('Aerospace Engineering'),
('Chemical Engineering');


CREATE TABLE admin (
    username VARCHAR(255),
    password VARCHAR(255)
);

INSERT INTO admin (username, password) VALUES ('admin', 'password123');

select*from admin;

	


