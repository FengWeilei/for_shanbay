# for_shanbay
Copyright (c) 2000, 2017, Oracle and/or its affiliates. All rights reserved.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> SHOW DATABASES;
+--------------------+
| Database           |
+--------------------+
| information_schema |
| FLASKAPP           |
| mysql              |
| performance_schema |
| sys                |
+--------------------+
5 rows in set (0.82 sec)

mysql> CREATE shanbay;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'shanbay' at line 1
mysql> CREATE DATABASE shanbay;
Query OK, 1 row affected (0.20 sec)

mysql> USE shanbay;
Database changed
mysql> CREATE TABLE users(id INT(11) AUTO_INCREMENT PRIMARY KEY, username VARCHAR(100),email VARCHAR(100), password VARCHAR(100), register_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP);
Query OK, 0 rows affected (0.88 sec)

mysql> SELECT * FROM users;
+----+----------+----------------+-------------------------------------------------------------------------------+---------------------+
| id | username | email          | password                                                                      | register_date       |
+----+----------+----------------+-------------------------------------------------------------------------------+---------------------+
|  1 | muhan    | muhan@0502.com | $5$rounds=535000$Lw58QX4Vw3OwLtqC$geK5VouwOxV2v.KsXThJa8dNccfWr22Ql64Tpum.2Y9 | 2017-08-13 21:03:31 |
+----+----------+----------------+-------------------------------------------------------------------------------+---------------------+
1 row in set (0.23 sec)

mysql> SELECT * FROM users;