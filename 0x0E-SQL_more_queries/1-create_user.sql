-- creat the MySQL server user user_0d_1.
-- Create user user_0d_1 if not exists
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost'
	IDENTIFIED BY 'user_0d_1_pwd';


SHOW GRANTS FOR 'user_0d_1'@'localhost';


FLUSH PRIVILEGES;
