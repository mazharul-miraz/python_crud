import sqlite3
import pdb


conn = sqlite3.connect('mydatabase.db');
print('Database opende')


conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
	VALUES (001,'Miraz', 23,'Chittagong', 500000)");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
	VALUES(002,'Vivien',25, 'Tokiyo', 7800000)");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
	VALUES(003,'mia',16, 'garmany', 7800000)");

conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
	VALUES(004,'cia',19, 'france', 7800000)");

conn.commit()
conn.close()