import sqlite3
import pdb


# SQLlite database operation 

conn = sqlite3.connect('mydatabase.db')
print('Opended Database Successfully');



conn.execute
('''CREATE TABLE COMPANY(
	ID INT PRIMARY KEY NOT NULL
	NAME TEXT NOT NULL
	AGE INT NOT NULL
	ADDRESS TEXT CHAR(50)
	SALARY REAL 
) ''')

print('table created successfully !')
conn.close()

# pdb.set_trace()