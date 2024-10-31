sql = '''

CREATE TABLE IF NOT EXISTS records (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	sitename TEXT NOT NULL,
	county TEXT,
	aqi INTEGER,
	status TEXT,
	pm25 NUMERIC,
	date TEXT,
	lat NUMERIC,
	lon NUMERIC
);'''


import sqlite3

#connect to SQLITE database
conn = sqlite3.connect('AQI_00.db')

#create a cursor object
cursor = conn.cursor()

#create a table
cursor.execute(sql)

#commit changes and close the connection
conn.commit()
cursor.close()
conn.close()
